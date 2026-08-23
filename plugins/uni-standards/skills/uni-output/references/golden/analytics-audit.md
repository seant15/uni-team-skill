# GOLDEN SAMPLE - Analytics & Tracking Audit (Google Doc)

> **Status:** anonymised from a real UNI tracking audit. Client name, domains, and every container, property and account ID are substituted. The structure and the reasoning are unchanged.
> **All pricing removed.** Never add it back.
> **Format:** Google Doc. Written to survive being commented on line by line - short paragraphs, one point each, numbers in tables.
> **Hard requirements at the bottom of this file.**

---

## Why this document is shaped the way it is

A tracking audit has two readers with opposite needs, and most agencies write for one and lose the other:

- **The client** wants to know what is broken, what it costs them, and what they have to do.
- **Their developer** wants a task list with exact IDs and code, and nothing else.

So the document splits into four sections, each addressed to one reader. **Never mix them.** A dev brief with strategy paragraphs in it gets skimmed, and the install gets done wrong.

| Section | Reader | Job |
|---|---|---|
| 1. Overview | Client decision-maker | What is broken, what we do, what you do, when |
| 2. Tracking strategy | Client + technical lead | The reasoning, the property inventory, the event model |
| 3. Developer brief | Developer only | Exact tasks, exact IDs, copy-paste code |
| 4. Reference | Everyone, later | Lookup tables for events, IDs, platforms |

---

# Harlow - Analytics & Tracking Implementation Plan

*Prepared by UNI Marketing Agency · [date] · seant@unimarketingagency.com*

This plan unifies analytics across Harlow's web properties and prepares the Google Ads account for accurate measurement. Your web team installs the tracking containers. UNI configures all event logic and validates it before we optimise campaigns.

---

## 1. Overview

### Executive summary

Harlow's web presence spans five properties on different platforms with inconsistent analytics. Three of them cannot currently be measured at all.

**Path A (primary).** Install Google Tag Manager container `GTM-XXXXXXX` on every property, plus custom event code where a platform does not emit the event natively. UNI configures all tracking inside GTM.

**Path B (fallback).** If GTM cannot go live on the care and outlet domains within week 1, install a temporary shared GA4 tag on those two. UNI bridges measurement until GTM is complete everywhere.

**GA4 consolidation.** Merge `G-AAAAAAAAAA` (main shop) and `G-BBBBBBBBBB` (outlet) into one property, so there is a single view of web performance instead of two partial ones.

### What we need from Harlow - week 1

1. Install `GTM-XXXXXXX` on showroom, care and outlet domains
2. Verify GTM is present on all main-site page templates
3. Install event tracking snippets for the triggers marked in the reference section
4. Grant UNI Editor access on Google Tag Manager
5. Tell UNI when each domain is live so QA can start

### What UNI handles

- All event configuration in GTM: retailer clicks, forms, phone and email, e-commerce, appointments, chat
- GA4 property consolidation and Google Ads linking
- Full QA validation before any campaign optimisation begins

### Timeline

| When | What |
|---|---|
| Week 1 | GTM live on all four domains |
| Week 1-2 | UNI configures events and runs QA, GA4 linked to Google Ads, campaign restructure begins |
| Week 3+ | Retire legacy Universal Analytics tags, finalise consolidated reporting |

---

## 2. Tracking strategy

### The problem

Harlow is not one website. It is five properties on different CMS stacks with different analytics IDs and duplicate legacy tags. Current analytics gives no unified view.

| Property | Events we want | Audit status |
|---|---|---|
| Physical showroom | calls, directions | needs business-profile and site tags |
| Big-box retail stores (offline) | ROAS | not in GA, use retail media platforms only |
| showroom domain | contact | no analytics in source |
| care domain | contact, appointment | legacy UA only, cached GTM mess |
| outlet domain | purchase, add to cart | separate GA4 property |
| find-dealer page | dealer navigation | the only clean pass in the audit |
| Retailer sites (online) | purchase | off-site, not measurable by us |

Additional finding: the main site fails Core Web Vitals (desktop 31, mobile 46). Logged as a separate backlog item, not part of this scope.

### Property inventory

| Property | Platform | Current tracking | Forms / chat |
|---|---|---|---|
| Main shop | WordPress + WooCommerce | GTM, legacy UA, GA4 `G-AAAAAAAAAA`, Google Ads tag, Meta Pixel | chat widget, booking plugin, Woo forms |
| Showroom | WordPress + page builder | none | contact form plugin |
| Support | WordPress + WooCommerce | legacy UA, Google Ads tag, cached GTM js | support tickets, booking plugin |
| Outlet | WordPress + WooCommerce | GA4 `G-BBBBBBBBBB` only, no GTM | Woo checkout |
| Find dealer | WordPress page | same as main shop | none |

### Two-path installation model

**Path A - GTM first (recommended).** Client dev installs the GTM snippet on every property. UNI configures all events inside GTM using hostname-based triggers.

| Site | Client installs | UNI configures |
|---|---|---|
| Main | verify existing GTM on all templates, add custom event code | retailer link clicks, Woo events, chat, bookings, tel and mailto |
| Showroom | new GTM snippet, custom event code | contact, tel, mailto, dealer hub clicks |
| Care | new GTM snippet, replacing the cached legacy file | contact, appointment, support form |
| Outlet | new GTM snippet, custom event code | add to cart, purchase, view item |

**Path B - GA4 direct (care and outlet only).** If the dev team cannot install GTM on those two in week 1, install one shared GA4 measurement ID on both. **Path B is a bridge, not the end state.** The target remains one GA4 property, not a third orphan.

### Event names by property

Standard names everywhere they apply. Consistency across properties matters more than any individual name being ideal.

| Event | Main | Showroom | Care | Outlet |
|---|---|---|---|---|
| `retailer_link_click` | P1 | via find-dealer | - | - |
| `click_to_call` | yes | yes | yes | yes |
| `click_to_email` | yes | yes | yes | yes |
| `contact_form_submit` | yes | yes | yes | optional |
| `appointment_booked` | yes | - | yes | - |
| `chat_open` | yes | if added | if added | if added |
| `view_item` | yes | - | - | yes |
| `add_to_cart` | yes | - | - | yes |
| `purchase` | yes (secondary) | - | - | yes (primary) |
| `find_dealer_view` | yes | - | - | - |
| `dealer_hub_click` | yes | yes | - | - |
| `scroll_depth` | yes | yes | yes | yes |

**E-commerce priority.** The outlet is the better store and the only place a full funnel is worth reporting. On the main site, track cart and purchase for completeness but **do not optimise Google Ads to direct-to-consumer** - the money is made at the retailers, so `retailer_link_click` is the primary signal.

That last paragraph is the most important one in the document. It is the difference between a tracking plan and a tracking plan that matches how the business actually makes money. Find that sentence for every client and put it in bold.

---

## 3. Developer brief

*Addressed to the web and development team. No strategy in this section.*

### Summary

Install the GTM container on each site. UNI configures all tracking logic afterwards. You do not need to build the event logic, only the containers and the custom event snippets listed below.

### Path A - install GTM on all sites (required)

Container ID: `GTM-XXXXXXX`

Sites needing a new install:

1. Showroom domain, all pages
2. Care domain, all pages, replacing the legacy cached file if present
3. Outlet domain, all pages

Install the standard snippet in `<head>` and immediately after `<body>`. Code below.

After GTM is live everywhere, remove or disable hardcoded duplicate tags. **Coordinate with UNI before removing any legacy tag** - we confirm in GTM Preview first.

### GTM installation code

```html
<!-- Google Tag Manager - place inside <head> -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXXX');</script>
```

```html
<!-- Google Tag Manager (noscript) - immediately after opening <body> -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-XXXXXXX"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
```

### Other development tasks

1. GTM on showroom, care, outlet
2. Grant UNI Editor on Google Tag Manager
3. Install custom event code for the transactional events flagged in the reference section
4. 301 redirect the plural find-dealers path to the singular find-dealer path
5. Core Web Vitals - separate backlog, not blocking

### Access UNI needs

| Tool | Permission |
|---|---|
| Google Tag Manager | Editor |
| WordPress | only if GTM cannot be used |

---

## 4. Reference

### Tracking IDs

| Tool | ID |
|---|---|
| GTM | `GTM-XXXXXXX` |
| GA4 (main) | `G-AAAAAAAAAA` |
| GA4 (outlet) | `G-BBBBBBBBBB` - merge target |
| Universal Analytics | `UA-XXXXXXXX-1` - retire |
| Google Ads | `AW-XXXXXXXXX`, CID `XXX-XXX-XXXX` |
| Meta Pixel | `XXXXXXXXXXXXXXX` |

### Off-property channels, not measurable in GA4

| Channel | Measurement |
|---|---|
| Retailer A retail media | their own platform's ROAS |
| Retailer B retail media | their own platform's ROAS |
| Physical retail stores | not trackable |
| Business profile listing | calls, directions, website clicks |

Naming that section honestly is what stops a client asking six months later why the numbers do not add up.

---

## Hard requirements

1. **Four sections, four readers, no mixing.** Strategy never appears in the developer brief.
2. **Every ID appears exactly as it must be typed.** In real documents these are live IDs. In anything shared beyond the client, they are substituted.
3. **State what cannot be measured**, in its own table, before the client discovers it themselves.
4. **One bolded sentence naming where the money is actually made**, and what that means for what we optimise toward.
5. **Findings carry evidence.** Audit status column, page speed scores, tag inventory - not adjectives.
6. **No pricing.** Scope and access requirements only.
7. **Zero em dashes and en dashes.** Hyphens only.
8. **Google Doc format:** short paragraphs, one point each, numbers in tables, written to be commented on.
9. **A fallback path for anything that depends on the client's dev team.** Path B exists because week-1 dev promises slip, and a plan with no fallback stalls the whole engagement.
