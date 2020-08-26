# Hurricane_Analysis

Analysing Atlantic Hurricanes

Hurricanes, also known as cyclones or typhoons. We are looking at data about the most powerful hurricanes that have occurred.

1) Begin by looking at the damages list. 
   The list contains strings representing the total cost in USD($) caused by 34 category 5 hurricanes (wind speeds ≥ 157 mph (252 km/h )) in the Atlantic region. 
   Damage data was not recorded ("Damages not recorded"), while the rest are written in the format "Prefix-B/M", where B stands for billions (100,00,00,000) and M stands for          millions (10,00,000).
 
 Aim:
 
 1) Written a function that returns a new list of updated damages where the recorded data is converted to float values and the missing data is retained.
 2) Additional data is collected and a function is written that constructs a dictionary made out of the lists, where the keys of the dictionary are the names of the hurricanes,     and the values are dictionaries themselves containing a key for each piece of data (Name, Month, Year,Max Sustained Wind, Areas Affected, Damage, Death) about the               hurricane.
 3) Written another function that iterates through each hurricane in our hurricanes dictionary, hurricanes, and records the year as current_year.
 4) Finding all affected areas across all hurricanes.
 5) Finding most affected area function by using above dictionary of affected areas count.
 6) Next, calculating the highest mortality hurricane and the number of deaths it caused.
 7) Also, catgeorize by mortality function by returning a dictionary with rates starting from 0 to 5 as keys and values. If deaths < 100, then assign values to keys(rates) ,           (check in hurricanes list).
      mortality_scale = {0: 0,
                         1: 100,
                         2: 500,
                         3: 1000,
                         4: 10000}

 8) Finding out the name of Hurricane and the greatest damage occured.
      damage_scale = {0: 0,
                      1: 100000000,
                      2: 1000000000,
                      3: 10000000000,
                      4: 50000000000}

 9) Finally, categorising the Hurricane again.
