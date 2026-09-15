/**
 * Apply UNI field-guide IR to a Google Doc using live paragraph indexes.
 * Never compute startIndex from a local text file.
 */
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);

function loadGoogle() {
  try {
    return require('googleapis');
  } catch {
    const extra = process.env.GOOGLEAPIS_NODE_PATH;
    if (extra) {
      const { createRequire: cr } = require('module');
      const abs = path.resolve(extra);
      const r = cr(path.join(abs, 'package.json'));
      return r('googleapis');
    }
    throw new Error(
      'Cannot load googleapis. Run from a folder that has it, or set GOOGLEAPIS_NODE_PATH to that folder.',
    );
  }
}

function parseArgs(argv) {
  const out = { ir: null, documentId: null, tabId: null, skeleton: false };
  for (let i = 0; i < argv.length; i += 1) {
    const a = argv[i];
    const next = argv[i + 1];
    if (a === '--ir') {
      out.ir = next;
      i += 1;
    } else if (a === '--document-id') {
      out.documentId = next;
      i += 1;
    } else if (a === '--tab-id') {
      out.tabId = next;
      i += 1;
    } else if (a === '--skeleton') {
      out.skeleton = true;
    }
  }
  return out;
}

function loadIr(filePath) {
  const raw = fs.readFileSync(filePath, 'utf8');
  if (/[\u2014\u2013]/.test(raw)) {
    throw new Error('IR contains an em dash or en dash. Use hyphen only.');
  }
  return JSON.parse(raw);
}

function flatten(ir) {
  const items = [];
  const push = (item) => {
    if (item.type === 'table') {
      items.push(item);
      return;
    }
    const text = String(item.text || '')
      .replace(/\r\n/g, '\n')
      .replace(/\n+/g, ' ')
      .trim();
    if (!text) return;
    items.push({ ...item, text });
  };

  if (ir.kicker) push({ type: 'kicker', style: 'NORMAL_TEXT', text: ir.kicker });
  if (ir.title) push({ type: 'title', style: 'TITLE', text: ir.title });
  if (ir.deck) push({ type: 'deck', style: 'SUBTITLE', text: ir.deck });

  for (const section of ir.sections || []) {
    if (section.kicker) push({ type: 'kicker', style: 'NORMAL_TEXT', text: section.kicker });
    const headingStyle = Number(section.headingLevel) === 2 ? 'HEADING_2' : 'HEADING_1';
    push({ type: 'h', style: headingStyle, text: section.heading });
    if (section.deck) {
      push({ type: 'deck', style: 'NORMAL_TEXT', text: section.deck, bold: true });
    }
    for (const block of section.blocks || []) {
      if (block.type === 'table') {
        items.push({
          type: 'table',
          headers: block.headers || [],
          rows: block.rows || [],
        });
        continue;
      }
      if (block.type === 'p') push({ type: 'p', style: 'NORMAL_TEXT', text: block.text });
      if (block.type === 'h') push({ type: 'h', style: 'HEADING_3', text: block.text });
      if (block.type === 'c') {
        push({ type: 'c', style: 'NORMAL_TEXT', text: block.text, checkbox: true });
      }
      if (block.type === 'box') {
        push({ type: 'box', style: 'NORMAL_TEXT', text: block.text, callout: true });
      }
    }
  }
  return items;
}

function renderTable(headers, rows) {
  const cols = headers.length;
  const lines = [
    `| ${headers.join(' | ')} |`,
    `| ${headers.map(() => '---').join(' | ')} |`,
  ];
  for (const row of rows) {
    const cells = [...row];
    while (cells.length < cols) cells.push('');
    lines.push(`| ${cells.slice(0, cols).join(' | ')} |`);
  }
  return lines.join('\n');
}

function renderSkeleton(items) {
  const lines = [];
  for (const item of items) {
    if (item.type === 'table') {
      if (lines.length && lines[lines.length - 1] !== '') lines.push('');
      lines.push(renderTable(item.headers, item.rows));
      lines.push('');
      continue;
    }
    lines.push(item.text);
    lines.push('');
  }
  return `${lines.join('\n').trim()}\n`;
}

function paragraphText(paragraph) {
  return (paragraph.elements || [])
    .map((el) => el.textRun?.content || '')
    .join('')
    .replace(/\r/g, '')
    .replace(/\u000b/g, ' ')
    .replace(/\n$/g, '')
    .trim();
}

function bodyOf(doc, tabId) {
  const tabs = doc.data.tabs || [];
  if (!tabs.length) return { body: doc.data.body, tabId: undefined };
  if (tabs.length > 1 && !tabId) {
    const names = tabs.map((t) => t.tabProperties?.title || t.tabProperties?.tabId);
    throw new Error(`Document has ${tabs.length} tabs. Pass --tab-id. Tabs: ${names.join(', ')}`);
  }
  const tab = tabId
    ? tabs.find((t) => t.tabProperties?.tabId === tabId)
    : tabs[0];
  if (!tab) throw new Error(`Tab not found: ${tabId}`);
  return {
    body: tab.documentTab?.body,
    tabId: tab.tabProperties?.tabId,
  };
}

function isSeparatorRow(line) {
  const cells = line.split('|').map((c) => c.trim()).filter(Boolean);
  return cells.length > 0 && cells.every((c) => /^:?-{3,}:?$/.test(c));
}

function parseRow(line) {
  const parts = line.split('|').map((c) => c.trim());
  if (parts[0] === '') parts.shift();
  if (parts[parts.length - 1] === '') parts.pop();
  return parts;
}

function findMarkdownTables(body) {
  const tables = [];
  let current = null;
  for (const element of body.content || []) {
    if (!element.paragraph) {
      if (current) {
        tables.push(current);
        current = null;
      }
      continue;
    }
    const trimmed = paragraphText(element.paragraph);
    if (trimmed.startsWith('|') && trimmed.includes('|', 1)) {
      if (isSeparatorRow(trimmed)) continue;
      const row = parseRow(trimmed);
      if (!current) {
        current = {
          startIndex: element.startIndex,
          endIndex: element.endIndex - 1,
          rows: [row],
        };
      } else {
        current.rows.push(row);
        current.endIndex = element.endIndex - 1;
      }
    } else if (current) {
      tables.push(current);
      current = null;
    }
  }
  if (current) tables.push(current);
  return tables;
}

function getTableCellStartIndices(table) {
  const indices = [];
  for (const row of table.tableRows || []) {
    const rowIndices = [];
    for (const cell of row.tableCells || []) {
      const content = cell.content?.[0];
      const paragraph = content?.paragraph;
      const firstEl = paragraph?.elements?.[0];
      rowIndices.push(firstEl?.startIndex ?? content?.startIndex ?? cell.startIndex);
    }
    indices.push(rowIndices);
  }
  return indices;
}

async function convertTable(docs, documentId, tabId, tableDef) {
  const numRows = tableDef.rows.length;
  const numCols = Math.max(...tableDef.rows.map((r) => r.length));
  const normalizedRows = tableDef.rows.map((r) => {
    const copy = [...r];
    while (copy.length < numCols) copy.push('');
    return copy;
  });

  const range = { startIndex: tableDef.startIndex, endIndex: tableDef.endIndex };
  if (tabId) range.tabId = tabId;
  const location = { index: tableDef.startIndex };
  if (tabId) location.tabId = tabId;

  await docs.documents.batchUpdate({
    documentId,
    requestBody: {
      requests: [
        { deleteContentRange: { range } },
        { insertTable: { rows: numRows, columns: numCols, location } },
      ],
    },
  });

  const doc = await docs.documents.get({ documentId, includeTabsContent: true });
  const { body } = bodyOf(doc, tabId);
  let insertedTable = null;
  for (const element of body.content || []) {
    if (element.table && element.startIndex >= tableDef.startIndex - 2) {
      insertedTable = element.table;
      break;
    }
  }
  if (!insertedTable) throw new Error(`Inserted table not found at ${tableDef.startIndex}`);

  const cellIndices = getTableCellStartIndices(insertedTable);
  const insertRequests = [];
  for (let r = 0; r < numRows; r += 1) {
    for (let c = 0; c < numCols; c += 1) {
      const index = cellIndices[r]?.[c];
      const text = normalizedRows[r][c] || '';
      if (index != null && text) {
        const loc = { index };
        if (tabId) loc.tabId = tabId;
        insertRequests.push({ insertText: { location: loc, text } });
      }
    }
  }
  insertRequests.sort((a, b) => b.insertText.location.index - a.insertText.location.index);
  if (insertRequests.length) {
    await docs.documents.batchUpdate({ documentId, requestBody: { requests: insertRequests } });
  }

  const refreshed = await docs.documents.get({ documentId, includeTabsContent: true });
  const refreshedBody = bodyOf(refreshed, tabId).body;
  let headerTable = null;
  for (const element of refreshedBody.content || []) {
    if (element.table && element.startIndex >= tableDef.startIndex - 2) {
      headerTable = element;
      break;
    }
  }
  if (headerTable?.table?.tableRows?.[0]) {
    const headerCells = getTableCellStartIndices(headerTable.table)[0];
    const styleRequests = [];
    for (let c = 0; c < numCols; c += 1) {
      const start = headerCells[c];
      const cellText = normalizedRows[0][c] || '';
      if (start != null && cellText) {
        const rangeReq = { startIndex: start, endIndex: start + cellText.length };
        if (tabId) rangeReq.tabId = tabId;
        styleRequests.push({
          updateTextStyle: {
            range: rangeReq,
            textStyle: { bold: true },
            fields: 'bold',
          },
        });
      }
    }
    if (styleRequests.length) {
      await docs.documents.batchUpdate({
        documentId,
        requestBody: { requests: styleRequests },
      });
    }
  }
  return { rows: numRows, cols: numCols };
}

function getAuth() {
  const { google } = loadGoogle();
  const configDir = path.join(os.homedir(), '.google-workspace-mcp');
  const tokenPath = path.join(configDir, 'tokens.json');
  const credPath =
    process.env.GOOGLE_CREDENTIALS_PATH ||
    path.join(configDir, 'oauth-client.json');
  if (!fs.existsSync(tokenPath)) {
    throw new Error(`Missing OAuth tokens: ${tokenPath}`);
  }
  if (!fs.existsSync(credPath)) {
    throw new Error(
      'Missing OAuth client JSON. Set GOOGLE_CREDENTIALS_PATH or place oauth-client.json in ~/.google-workspace-mcp/',
    );
  }
  const keys = JSON.parse(fs.readFileSync(credPath, 'utf8'));
  const key = keys.installed || keys.web;
  const tokens = JSON.parse(fs.readFileSync(tokenPath, 'utf8'));
  const oauth2 = new google.auth.OAuth2(
    key.client_id,
    key.client_secret,
    key.redirect_uris?.[0],
  );
  oauth2.setCredentials(tokens);
  return { google, auth: oauth2 };
}

function expectedCounts(items) {
  const counts = { TITLE: 0, SUBTITLE: 0, HEADING_1: 0, HEADING_2: 0, HEADING_3: 0, TABLE: 0 };
  for (const item of items) {
    if (item.type === 'table') counts.TABLE += 1;
    else if (counts[item.style] != null) counts[item.style] += 1;
  }
  return counts;
}

function actualCounts(body) {
  const counts = {
    TITLE: 0,
    SUBTITLE: 0,
    HEADING_1: 0,
    HEADING_2: 0,
    HEADING_3: 0,
    NORMAL_TEXT: 0,
    TABLE: 0,
  };
  for (const el of body.content || []) {
    if (el.table) counts.TABLE += 1;
    if (el.paragraph) {
      const style = el.paragraph.paragraphStyle?.namedStyleType || 'UNKNOWN';
      counts[style] = (counts[style] || 0) + 1;
    }
  }
  return counts;
}

async function applyStyles(docs, documentId, tabId, items) {
  const doc = await docs.documents.get({ documentId, includeTabsContent: true });
  const { body, tabId: resolvedTab } = bodyOf(doc, tabId);
  const paragraphs = (body.content || []).filter((el) => el.paragraph);
  const nonTable = items.filter((item) => item.type !== 'table');
  const requests = [];
  const used = new Set();

  for (const item of nonTable) {
    const pIndex = paragraphs.findIndex(
      (el, i) => !used.has(i) && paragraphText(el.paragraph) === item.text,
    );
    const el = pIndex >= 0 ? paragraphs[pIndex] : null;
    if (!el) {
      throw new Error(
        `Live paragraph not found for "${item.text.slice(0, 80)}". documents.get first; do not guess indexes.`,
      );
    }
    used.add(pIndex);
    const end = el.endIndex;
    const start = el.startIndex;
    const range = { startIndex: start, endIndex: end - 1 };
    if (resolvedTab) range.tabId = resolvedTab;
    const paragraphStyle = { namedStyleType: item.style };
    let paraFields = 'namedStyleType';
    if (item.callout) {
      paragraphStyle.shading = {
        backgroundColor: {
          color: { rgbColor: { red: 237 / 255, green: 242 / 255, blue: 241 / 255 } },
        },
      };
      paraFields = 'namedStyleType,shading';
    }
    requests.push({
      updateParagraphStyle: {
        range,
        paragraphStyle,
        fields: paraFields,
      },
    });
    if (item.bold || item.callout) {
      const textStyle = {};
      const fields = [];
      if (item.bold) {
        textStyle.bold = true;
        fields.push('bold');
      }
      if (item.callout) {
        textStyle.italic = true;
        fields.push('italic');
      }
      requests.push({
        updateTextStyle: {
          range,
          textStyle,
          fields: fields.join(','),
        },
      });
    }
    if (item.checkbox) {
      requests.push({
        createParagraphBullets: {
          range,
          bulletPreset: 'BULLET_CHECKBOX',
        },
      });
    }
  }

  if (requests.length) {
    await docs.documents.batchUpdate({ documentId, requestBody: { requests } });
  }
  return resolvedTab;
}

async function convertAllTables(docs, documentId, tabId) {
  const converted = [];
  while (true) {
    const current = await docs.documents.get({ documentId, includeTabsContent: true });
    const { body, tabId: resolvedTab } = bodyOf(current, tabId);
    const pending = findMarkdownTables(body);
    if (!pending.length) break;
    pending.sort((a, b) => b.startIndex - a.startIndex);
    converted.push(await convertTable(docs, documentId, resolvedTab, pending[0]));
  }
  return converted;
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (!args.ir) throw new Error('Usage: --ir file.json [--document-id ID] [--tab-id TAB] [--skeleton]');
  const ir = loadIr(args.ir);
  const items = flatten(ir);
  if (args.skeleton) {
    process.stdout.write(renderSkeleton(items));
    return;
  }
  if (!args.documentId) throw new Error('--document-id is required unless --skeleton');

  const { google, auth } = getAuth();
  const docs = google.docs({ version: 'v1', auth });

  const tables = await convertAllTables(docs, args.documentId, args.tabId);
  await applyStyles(docs, args.documentId, args.tabId, items);

  const verify = await docs.documents.get({
    documentId: args.documentId,
    includeTabsContent: true,
  });
  const { body } = bodyOf(verify, args.tabId);
  const expected = expectedCounts(items);
  const actual = actualCounts(body);
  const misses = [];
  for (const key of Object.keys(expected)) {
    if ((actual[key] || 0) < expected[key]) {
      misses.push(`${key} expected ${expected[key]} got ${actual[key] || 0}`);
    }
  }
  const report = {
    documentId: args.documentId,
    url: `https://docs.google.com/document/d/${args.documentId}/edit`,
    tablesConverted: tables.length,
    expected,
    actual,
    misses,
  };
  console.log(JSON.stringify(report, null, 2));
  if (misses.length) {
    console.error(`Doc styles: P1=${misses.length}`);
    process.exit(1);
  }
  const bits = Object.entries(expected)
    .filter(([, n]) => n)
    .map(([k, n]) => `${k}=${actual[k] || 0}`);
  console.error(`Doc styles: ${bits.join(' ')} P1=0`);
}

main().catch((err) => {
  console.error(err.message || err);
  process.exit(1);
});
