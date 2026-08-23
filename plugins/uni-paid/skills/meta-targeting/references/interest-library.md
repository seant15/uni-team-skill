# UNI basic interest library

**Source:** eachspy.com/facebook-ads-interests (third-party aggregator, states it pulls from Meta's Marketing API)
**Captured:** 2026-08-23 · **302 interests · 9 categories**
**Status of every row below: `unconfirmed`.** Nothing here has been validated against Ads Manager or the Marketing API yet.

---

## Read this before using a single row

**Three limitations, all of them load-bearing:**

**1. Names only, no IDs.** The source does not publish Meta interest IDs. Meta renames interests without notice, so a name-keyed list rots. Every row you actually use must be looked up and its **ID recorded** back into this file. See the schema below.

**2. Audience sizes are the aggregator's, not Meta's.** Treat them as order-of-magnitude only. Never quote one to a client as a Meta figure. Get the real number from the Ads Manager estimate at the moment you build the ad set.

**3. This is the obvious layer, on purpose.** These 302 are Meta's published top-level taxonomy. Every agency bidding in your category can find "Coffee" and "Running." **The competitive value of this file is as a seed vocabulary for the interest web in `SKILL.md`, not as a targeting list.** If a deliverable contains only interests from this file, the method was not applied.

Read `platform-reality-2026.md` for why no complete list exists and what Meta removed in the January 2026 consolidation. Several rows below may already be dead.

---

## Why we keep a library at all

Sean's position, and it is the right one: Advantage+ detailed targeting means Meta delivers beyond whatever we select, **but the interest still tells Meta which direction to start looking.** Two ad sets seeded differently do not perform identically, and that difference is readable. That is the strategy.

Three jobs:

1. **Shared vocabulary.** Two buyers on one account reach for the same names instead of each inventing their own.
2. **Expansion seed.** The interest web is only as good as what it expands from. A blank page produces the five obvious interests.
3. **Differentiator.** Everyone can find "Coffee." Very few teams maintain a set that reaches two steps out. That set is the asset, and it gets built on top of this file.

---

## Working schema

When a row graduates from this list into real use, record it in the validated table at the bottom. **The ID is the key.**

| Field | Notes |
|---|---|
| `id` | Meta interest ID. Primary key. Required before client use. |
| `name` | Display name at capture. Will drift. |
| `path` | Taxonomy breadcrumb from the API `path` array |
| `category` | Demographics / Interests / Behaviors |
| `dimension` | Interest-web dimension: media / people / gear / home / work / retail / events |
| `audience_lower` `audience_upper` | From Ads Manager or the API, not from this file |
| `captured` `last_validated` | Dates |
| `status` | `live` / `unconfirmed` / `dead` |
| `source` | scrape / API / Ads Manager / teammate |

Rows are never deleted. A dead interest stays with `status: dead` and its date, so nobody re-adds it next quarter and so we can watch what Meta is pruning.

### Validation

**Ads Manager:** type the name into the detailed targeting search box. Absent means gone. Record the audience size and the ID.

**Marketing API:**

```
GET /v26.0/search?type=adinterest&q=<name>&limit=1000&locale=en_US
GET /v26.0/search?type=adinterestvalid&interest_list=["<name>"]
GET /v26.0/act_<ID>/targetingvalidation?targeting_list=[{'type':'interests','id':<id>}]
```

**Quarterly sweep** of every validated row, plus an immediate sweep after any Meta consolidation notice. Anything older than a quarter is a lead, not a fact.

---

## Validated interests

Populated as rows graduate out of the seed list below. Empty until the first validation pass runs.

| id | name | dimension | audience | validated | status |
|---|---|---|---|---|---|

---

## Seed list - 302 interests, all `unconfirmed`

Audience figures are the aggregator's. Use for rough scale only.

## Business and industry

| Interest | Audience |
|---|---|
| Advertising | 466M-548M |
| Agriculture | 390M-458M |
| Architecture | 434M-510M |
| Aviation | 164M-193M |
| Banking | 429M-504M |
| Business | 997M-1.2B |
| Construction | 466M-548M |
| Design | 920M-1.1B |
| Economics | 309M-363M |
| Engineering | 470M-552M |
| Entrepreneurship | 382M-449M |
| Higher education | 563M-663M |
| Management | 332M-391M |
| Marketing | 605M-712M |
| Online | 1.1B-1.4B |
| Personal finance | 730M-858M |
| Real estate | 425M-499M |
| Retail | 713M-838M |
| Sales | 892M-1.0B |
| Science | 600M-706M |
| Small business | 177M-208M |
| Investment banking | 33M-38M |
| Online banking | 91M-106M |
| Retail banking | 24M-28M |
| Fashion design | 347M-409M |
| Graphic design | 315M-371M |
| Interior design | 488M-574M |
| Digital marketing | 149M-176M |
| Email marketing | 14M-17M |
| Online advertising | 156M-184M |
| Search engine optimization | 36M-43M |
| Social media | 634M-745M |
| Social media marketing | 84M-99M |
| Web design | 54M-63M |
| Web development | 46M-54M |
| Web hosting | 24M-28M |
| Credit cards | 435M-511M |
| Insurance | 340M-400M |
| Investment | 413M-485M |
| Mortgage loans | 144M-170M |

## Entertainment

| Interest | Audience |
|---|---|
| Entertainment | 1.8B-2.1B |
| Games | 1.2B-1.5B |
| Live events | 956M-1.1B |
| Movies | 1.4B-1.7B |
| Music | 1.5B-1.8B |
| Reading | 1.3B-1.5B |
| TV | 990M-1.2B |

### Games

| Interest | Audience |
|---|---|
| Action games | 153M-180M |
| Board games | 88M-103M |
| Browser games | 52M-61M |
| Card games | 272M-320M |
| Casino games | 43M-51M |
| First-person shooter games | 559M-657M |
| Gambling | 331M-390M |
| Massively multiplayer online games | 111M-131M |
| Massively multiplayer online role-playing games | 110M-129M |
| Online games | 596M-700M |
| Online poker | 151M-178M |
| Puzzle video games | 288M-339M |
| Racing games | 123M-145M |
| Role-playing games | 152M-179M |
| Simulation games | 93M-109M |
| Sports games | 168M-198M |
| Strategy games | 57M-67M |
| Video games | 946M-1.1B |
| Word games | 62M-73M |

### Live events

| Interest | Audience |
|---|---|
| Ballet | 100M-118M |
| Bars | 294M-346M |
| Concerts | 260M-306M |
| Dancehalls | 103M-122M |
| Music festivals | 293M-345M |
| Nightclubs | 335M-393M |
| Parties | 384M-452M |
| Plays | 206M-242M |
| Theatre | 513M-603M |

### Movies

| Interest | Audience |
|---|---|
| Action movies | 627M-738M |
| Animated movies | 419M-492M |
| Anime movies | 386M-453M |
| Bollywood movies | 375M-441M |
| Comedy movies | 1.0B-1.2B |
| Documentary movies | 440M-518M |
| Drama movies | 473M-557M |
| Horror movies | 377M-443M |
| Musical theatre | 99M-117M |
| Science fiction movies | 364M-427M |
| Thriller movies | 553M-650M |

### Music

| Interest | Audience |
|---|---|
| Blues music | 454M-534M |
| Classical music | 324M-381M |
| Country music | 471M-553M |
| Dance music | 286M-336M |
| Electronic music | 763M-898M |
| Heavy metal music | 604M-710M |
| Hip hop music | 824M-969M |
| Jazz music | 462M-544M |
| Music videos | 985M-1.2B |
| Pop music | 995M-1.2B |
| Rhythm and blues music | 669M-787M |
| Rock music | 959M-1.1B |
| Soul music | 461M-542M |

### Reading

| Interest | Audience |
|---|---|
| Books | 581M-684M |
| Comics | 285M-335M |
| E-books | 367M-431M |
| Fiction books | 408M-479M |
| Literature | 373M-439M |
| Magazines | 613M-721M |
| Manga | 226M-266M |
| Mystery fiction | 147M-173M |
| Newspapers | 815M-959M |
| Non-fiction books | 37M-43M |
| Romance novels | 230M-270M |

### TV

| Interest | Audience |
|---|---|
| TV game shows | 111M-130M |
| TV reality shows | 521M-612M |
| TV talkshows | 131M-155M |

## Family and relationships

| Interest | Audience |
|---|---|
| Family | 1.0B-1.2B |
| Fatherhood | 353M-415M |
| Friendship | 716M-843M |
| Marriage | 234M-275M |
| Motherhood | 698M-821M |
| Parenting | 284M-334M |
| Weddings | 305M-359M |

## Fitness and wellness

| Interest | Audience |
|---|---|
| Fitness and wellness | 1.1B-1.3B |
| Bodybuilding | 196M-231M |
| Physical exercise | 647M-761M |
| Physical fitness | 679M-798M |
| Running | 296M-348M |
| Weight training | 192M-225M |
| Yoga | 382M-450M |

## Food and drink

| Interest | Audience |
|---|---|
| Food and drink | 1.3B-1.6B |
| Alcoholic beverages | 533M-627M |
| Beverages | 855M-1.0B |
| Cooking | 753M-885M |
| Cuisine | 590M-694M |
| Food | 1.2B-1.4B |
| Restaurants | 730M-859M |

### Alcoholic beverages

| Interest | Audience |
|---|---|
| Beer | 333M-392M |
| Distilled beverage | 205M-240M |
| Wine | 332M-391M |

### Beverages

| Interest | Audience |
|---|---|
| Coffee | 536M-630M |
| Energy drinks | 98M-115M |
| Juice | 224M-263M |
| Soft drinks | 187M-220M |
| Tea | 395M-465M |

### Cooking

| Interest | Audience |
|---|---|
| Baking | 356M-419M |
| Recipes | 481M-565M |

### Cuisine

| Interest | Audience |
|---|---|
| Chinese cuisine | 152M-179M |
| French cuisine | 89M-105M |
| German cuisine | 29M-34M |
| Greek cuisine | 32M-37M |
| Indian cuisine | 92M-108M |
| Italian cuisine | 147M-172M |
| Japanese cuisine | 136M-160M |
| Korean cuisine | 102M-120M |
| Latin American cuisine | 42M-49M |
| Mexican cuisine | 103M-121M |
| Middle Eastern cuisine | 28M-33M |
| Spanish cuisine | 36M-42M |
| Thai cuisine | 57M-67M |
| Vietnamese cuisine | 48M-57M |

### Food

| Interest | Audience |
|---|---|
| Barbecue | 348M-409M |
| Chocolate | 475M-559M |
| Desserts | 399M-469M |
| Fast food | 446M-524M |
| Organic food | 273M-321M |
| Pizza | 442M-519M |
| Seafood | 270M-318M |
| Veganism | 325M-382M |
| Vegetarianism | 208M-244M |

### Restaurants

| Interest | Audience |
|---|---|
| Coffeehouses | 412M-484M |
| Diners | 118M-139M |
| Fast casual restaurants | 127M-150M |
| Fast food restaurants | 170M-200M |

## Hobbies and activities

| Interest | Audience |
|---|---|
| Arts and music | 1.4B-1.6B |
| Current events | 880M-1.0B |
| Pets | 896M-1.1B |
| Politics and social issues | 1.0B-1.2B |
| Travel | 1.2B-1.4B |
| Vehicles | 847M-996M |

### Arts and music

| Interest | Audience |
|---|---|
| Acting | 196M-230M |
| Crafts | 424M-498M |
| Dance | 546M-642M |
| Drawing | 198M-233M |
| Drums | 116M-137M |
| Fine art | 140M-165M |
| Guitar | 150M-177M |
| Painting | 402M-473M |
| Performing arts | 431M-507M |
| Photography | 1.1B-1.3B |
| Sculpture | 132M-155M |
| Singing | 426M-501M |
| Writing | 342M-402M |

### Home and garden

| Interest | Audience |
|---|---|
| Do it yourself | 418M-492M |
| Furniture | 522M-614M |
| Gardening | 356M-419M |
| Home Appliances | 265M-312M |
| Home improvement | 336M-395M |

### Pets

| Interest | Audience |
|---|---|
| Birds | 353M-415M |
| Cats | 448M-527M |
| Dogs | 492M-578M |
| Fish | 322M-378M |
| Horses | 258M-304M |
| Pet food | 108M-127M |
| Rabbits | 115M-135M |
| Reptiles | 49M-58M |

### Politics and social issues

| Interest | Audience |
|---|---|
| Charity and causes | 65M-76M |
| Community issues | 236M-278M |
| Law | 478M-562M |
| Politics | 461M-542M |
| Volunteering | 77M-90M |

### Travel

| Interest | Audience |
|---|---|
| Adventure travel | 275M-324M |
| Air travel | 306M-360M |
| Beaches | 413M-486M |
| Car rentals | 154M-181M |
| Cruises | 173M-203M |
| Ecotourism | 124M-146M |
| Hotels | 603M-710M |
| Lakes | 169M-198M |
| Mountains | 310M-364M |
| Nature | 815M-959M |
| Theme parks | 199M-235M |
| Tourism | 773M-909M |
| Vacations | 313M-368M |

### Vehicles

| Interest | Audience |
|---|---|
| Automobiles | 677M-797M |
| Boats | 146M-171M |
| Electric vehicle | 98M-115M |
| Hybrids | 64M-75M |
| Minivans | 49M-57M |
| Motorcycles | 416M-489M |
| RVs | 53M-63M |
| SUVs | 232M-273M |
| Scooters | 116M-137M |
| Trucks | 272M-320M |

## Shopping and fashion

| Interest | Audience |
|---|---|
| Beauty | 1.3B-1.5B |
| Clothing | 1.2B-1.4B |
| Fashion accessories | 978M-1.2B |
| Shopping | 1.4B-1.7B |
| Toys | 481M-565M |
| Beauty salons | 618M-727M |
| Cosmetics | 954M-1.1B |
| Fragrances | 557M-655M |
| Hair products | 726M-853M |
| Spas | 589M-692M |
| Tattoos | 496M-583M |
| Children's clothing | 262M-308M |
| Men's clothing | 456M-536M |
| Shoes | 841M-990M |
| Women's clothing | 598M-703M |
| Dresses | 573M-674M |
| Handbags | 413M-486M |
| Jewelry | 722M-849M |
| Sunglasses | 371M-436M |
| Boutiques | 533M-627M |
| Coupons | 578M-679M |
| Discount stores | 394M-463M |
| Luxury goods | 674M-792M |
| Online shopping | 1.3B-1.6B |
| Shopping malls | 588M-692M |

## Sports and outdoors

| Interest | Audience |
|---|---|
| Outdoor recreation | 581M-684M |
| Sports | 1.4B-1.7B |

### Outdoor recreation

| Interest | Audience |
|---|---|
| Boating | 77M-90M |
| Camping | 240M-282M |
| Fishing | 279M-328M |
| Horseback riding | 103M-121M |
| Hunting | 202M-237M |
| Mountain biking | 95M-111M |
| Surfing | 126M-148M |

### Sports

| Interest | Audience |
|---|---|
| American football | 418M-491M |
| Association football | 1.2B-1.5B |
| Auto racing | 316M-372M |
| Baseball | 451M-530M |
| Basketball | 714M-840M |
| College football | 107M-125M |
| Golf | 264M-311M |
| Marathons | 190M-223M |
| Skiing | 141M-166M |
| Snowboarding | 109M-129M |
| Swimming | 228M-268M |
| Tennis | 330M-388M |
| Triathlons | 95M-112M |
| Volleyball | 342M-402M |

## Technology

| Interest | Audience |
|---|---|
| Technology | 1.5B-1.8B |
| Computers | 1.2B-1.4B |
| Consumer electronics | 1.4B-1.6B |
| Computer memory | 35M-41M |
| Computer monitors | 145M-171M |
| Computer processors | 186M-219M |
| Computer servers | 87M-103M |
| Desktop computers | 156M-183M |
| Free software | 561M-660M |
| Hard drives | 122M-144M |
| Network storage | 19M-22M |
| Software | 926M-1.1B |
| Tablet computers | 513M-603M |
| Audio equipment | 44M-52M |
| Camcorders | 19M-22M |
| Cameras | 436M-512M |
| E-book readers | 46M-54M |
| GPS devices | 25M-29M |
| Mobile phones | 1.0B-1.2B |
| Portable media players | 7.0M-8.2M |
| Projectors | 32M-37M |
| Smartphones | 790M-929M |
| Televisions | 1.1B-1.3B |

---

## Using this file with the interest web

The seed list maps onto the interest-web dimensions like this. **Notice how thin the coverage is - that is the point.**

| Dimension | What the seed list gives you | What it does not |
|---|---|---|
| Media | Magazines, Newspapers, Books, Comics, Music videos | Any specific publication, channel, podcast or show |
| People | nothing | Every celebrity, author, founder and athlete |
| Gear | Cameras, Guitar, Boats, Furniture | Every brand, every specific tool |
| Home | Home improvement, Furniture, Gardening, Home Appliances | Every retailer and design brand |
| Work | Engineering, Marketing, Real estate, Higher education | Job titles, employers, software |
| Retail | Online shopping, Discount stores, Boutiques, Luxury goods | Every actual retailer |
| Events | Concerts, Music festivals, Marathons | Every specific event and community |

**Named entities - people, publications, brands, employers, schools - are where the two-step layer lives, and none of them are in this file.** Find them by searching Ads Manager or the Marketing API directly, using the method in `SKILL.md`. When you validate one, add it to the validated table at the top, tagged with its dimension. That table is what becomes genuinely valuable over time. This seed list never will be.
