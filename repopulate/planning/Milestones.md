# V1
- A massive decentralized/empty state and 88 equal-ish nations placed on coastlines, with colonial affairs enabled and 200k pops.
- Adds a lumberyard, port, shipyard, trade center and fishing pier to add the nation capitals.

### Play Session Result (~30 years)
- The AI has issues starting, always building 4-6 construction yards and then repeatedly goes bankrupt.
- The AI colonizes properly and this gives it options, later on.
- After 10-20 years, most of the AIs are blocked but some have managed to build luxury good farms or resources exploitation and that makes them compete slightly with the player.
- The player's main challenge: dealing with the low population, once he figures out that he shouldn't build any construction yard.
- Colonization goes faster than the population rises, which gives infrastructure issues. Research also appears faster than the player can take advantage of.

# V2
- Added a new building, the generation ship with some food and a birth rate boost helps the countries start.

### Play Session Result
- The AI still has significant issues growing its economy, due to the cost of fabric.
- The Player can fix most of his issues by eventually colonizing on multiple continents.

# V3
- Added a population boost at the capital and a general birth boost at the start of the game.
- Varied the two economic and food production buildings so that there are more trades and more fabric at the start of the game.

### Play Session Result (~40 years)
- The Player has some interesting decisions to make and can play quite fast.
- In my test run of Wales, population management still became a problem, but only after infrastructure. Lack of infrastructure can be fixed with ports, but inland states don't have any infrastructure growth until the railroad.
- An astute player would win very easily by building up militarily.
- The AI does manage to build interesting countries, focusing mostly on trade and luxury resources.
- The technology doesn't seem to go faster than the player anymore.
- It feels like autocracy is the reason that the AIs fail: they don't change very fast from their original strategy that isn't military.

### AI-only Simulation to 1936 Review
- The construction industry is still breaking the states at the start. This may be due to the low construction produced by the AI states. Looks like there is an option to force construction to 10 rather than based on GDP?
- After a while, the simulation starts to randomly produce greatness, like a tool workshop in one country, then a different country starts using tools in their lumberyard... It takes a while for production chains to build. They seem mostly random.
- The total population is still very small after 80 years. Some regions like China and India have only a few million persons.
- After 80 years, the map isn't fully colonized either.
- There have been few wars, rebellions mostly. I'm starting to see a few neighbor wars in 1917: Louisiana vs Rio Grande, Zealand vs Svealand...
- Technology is also years behind, not just buildings.
- In 1936, Guangdong has the GDP lead with 11.1M, followed by Pegu at 7.5M. There are only 9 countries with their GDP > 4.0M. In terms of population, Bengal leads with 12.2M, followed by Gujarat at 10.5M. There are 12 countries with a population > 5M. South Angola has the top Standard of Living with 13.0, followed by Bolivar at 12.0. Most countries are in the 9.5-10.5 range.

### Base Victoria Start Conditions
- Some statistics from starting a vanilla game of Victoria 3: in 1836, the Great Qing has 366M people, the East India Company is second with 110M people. Some quick math, there are maybe ~900M people at start. This compares to my start with 88x200k = 17.6M people. In terms of GDP, the situation is similar. The Great Qing has 85.6M GDP, the East India company has 34.7M GDP. The world GDP looks to be ~350M. In my MOD, the start GDP is tiny, maybe 150k$ per country for a total of 13M.

# V4
- Set "Base Construction Capacity" to "Maximum".
- Added an army with 1 unit and 5 conscript to each country.
- Removed the fruit production on the generation ship.
- Add random start strategies instead of all the same.
- Boost birth rate through the generation ship. The birth rate is now +300% for 20 years and then +100% on the capital.
- Boost colonization through the generation ship and emigration. The generation ship now provides x10 colony growth speed.
- Added a second trade center to each capital.

### AI-only Simulation 1
- The AI still starts by building a bunch of construction industries. This quickly expands their treasury and then they stop building.
- After 20 years, the cloning vats modifier expires and the world population has risen to about 300M. It has risen too fast and most countries are starving, there are many rebellions, taxation capacity is significantly lowered. Maybe this is an interesting early game dynamic? Countries with a large space for subsistence fared much better.
- After 20 years, colonization is dramatically more advanced than before. It could be a bit faster, maybe, to allow countries to get more subsistence farming?

### AI-only Simulation 2
- Added 20 construction to the generation ship production. Also set its production to boost colonization to 10 and emigration to -0.4.
- Didn't work to add construction directly on the generation ship. The boost in colonization and emigration are working though.
- Injecting a custom routine in the AI default strategy does work to fix the construction problem. What would be a good routine for the # of construction yards?


# Later Ideas
- Change the law away from autocracy to give the AI more different leaders over time, "landed voting"?
- Standardize the cultural "homelands" based on the placed cultures (low).
- Reviewing the world after 10-15 years: the construction is blocked by a complete lack of iron. Should I add some tool workshops or iron mines? Maybe have 2 economic and 2 agricultural buildings for each nation?
- How can I equilize nations where the states in China/India have 300-400 fertile lands, while ALL OF western australia has less than 10?

# V4
