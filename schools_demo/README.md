Notes:
1. This uses the dataset from [National Center for Education Statistics](https://nces.ed.gov/ccd/CCDLocaleCode.asp); specifically _Year 2005-2006 (v.1b), States A-I, ZIP (769 KB) CSV File_.
2. Loosely follows this [documentation](https://nces.ed.gov/ccd/pdf/sl051bgen.pdf) 
3. There is a typo in the csv file. For one of the rows, there is a state code called 'C'. I think they meant 'DC'. Mapped it accordingly in the code.
4. This creates in-memory cache of dataset on initialization, based on school name and location information. New requests are served from the cache. Cache expiration and invalidations aren't implemented.
5. Search results by themselves aren't cached. Only the underlying data is.  


Usage:

**school_search.search_schools** interface pulls the top 3 schools based on the search text
```
>>> school_search.search_schools("elementary school highland park")
Results for "elementary school highland park" (search took: 0.04300602s)
1. HIGHLAND PARK ELEMENTARY SCHOOL
MUSCLE SHOALS, AL
2. HIGHLAND PARK ELEMENTARY SCHOOL
PUEBLO, CO
3. BLUFF PARK ELEMENTARY SCHOOL
HOOVER, AL
```
```
>>> school_search.search_schools("jefferson belleville")
Results for "jefferson belleville" (search took: 0.001362624s)
1. JEFFERSON ELEM SCHOOL
BELLEVILLE, IL
2. JEFFERSON COUNTY COUNSELING LEARNING CENTER-EAST
BIRMINGHAM, AL
3. WEST JEFFERSON ELEMENTARY SCHOOL
QUINTON, AL
```
```
>>> school_search.search_schools("riverside school 44")
Results for "riverside school 44" (search took: 0.002020411s)
1. RIVERSIDE SCHOOL 44
INDIANAPOLIS, IN
2. RIVERSIDE ELEMENTARY SCHOOL
PHOENIX, AZ
3. RIVERSIDE EAST ELEM. SCHOOL
CARAWAY, AR
```
```
>>> school_search.search_schools("granada charter school")
Results for "granada charter school" (search took: 0.005279595s)
1. GRANADA HILLS CHARTER HIGH
GRANADA HILLS, CA
2. NORTH VALLEY CHARTER ACADEMY
GRANADA HILLS, CA
3. GRANADA EAST SCHOOL
PHOENIX, AZ
```
```
>>> school_search.search_schools("foley high alabama")
Results for "foley high alabama" (search took: 0.031057229s)
1. FOLEY HIGH SCHOOL
FOLEY, AL
2. FOLEY MIDDLE SCHOOL
FOLEY, AL
3. FOLEY ELEMENTARY SCHOOL
FOLEY, AL
```
```
>>> school_search.search_schools("KUSKOKWIM")
Results for "KUSKOKWIM" (search took: 9.7317e-05s)
1. TOP OF THE KUSKOKWIM SCHOOL
NIKOLAI, AK
>>> 
```

Alternatively, one could also use the **service.school_service.school_search_service.search_schools**. This takes a num_results parameter additionally, so if you need more than 3 results, this would be a more appropriate one. However, it ensures that you can't ask for more than 10 results at a time.
