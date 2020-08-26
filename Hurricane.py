# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages in (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here: converting values of damages to float and stripping M and B
def update_damages(damage):
    conversion = {"M": 1000000, "B": 1000000000}
    damages_in_float = []
    for damage in damages:
        if damage == "Damages not recorded":
            damages_in_float.append(damage)
        elif damage[-1] == "M" :
            damages_in_float.append(float(damage.strip('M')) * conversion["M"]) #stripped M and converted to float and then multiplied with conversion values
        elif damage[-1] == "B":
            damages_in_float.append(float(damage.strip('B')) * conversion["B"])
    return damages_in_float
      
#print(update_damages(damages))
update_damages = update_damages(damages)

# Creating new dictionary
def hurricane(names, months, years, max_sustained_winds, areas_affected, update_damages, deaths):
    hurricane_data = {}
    for i in range(0, len(names)):
        hurricane_data[names[i]] = {    "Name": names[i],
                                        "Month": months[i],
                                        "Year": years[i],
                                        "Max Sustained Wind": max_sustained_winds[i],
                                        "Areas Affected": areas_affected[i],
                                        "Damage": update_damages[i],
                                        "Deaths": deaths[i]  
                                    }

    return hurricane_data
hurricanes = hurricane(names, months, years, max_sustained_winds, areas_affected, update_damages, deaths)
print(hurricanes)

# creating new dictionary as per year
def hurricane_year(names, months, years, max_sustained_winds, areas_affected, update_damages, deaths):
    hurricane_list_yearly = []
    for names, months, years, max_sustained_winds, areas_affected, update_damages, deaths in zip(names, months, years, max_sustained_winds, areas_affected, update_damages, deaths):
        
        dict  = { years:   { "Name": names,
                            "Month": months,
                            "Year": years,
                            "Max Sustained Wind": max_sustained_winds,
                            "Areas Affected": areas_affected,
                            "Damage": update_damages,
                            "Deaths": deaths  }
                }
    
        hurricane_list_yearly.append(dict)
    return hurricane_list_yearly
    
#print(hurricane_year(names, months, years, max_sustained_winds, areas_affected, update_damages, deaths))


# Finding the count of affected areas across all hurricanes and return as a dictionary with the affected areas as keys.
def affected_areas_count(areas_affected):
    count = {}
    for areas in areas_affected:
        for i in areas:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
    return count
affected_areas_count = affected_areas_count(areas_affected)
#print(affected_areas_count)

#Finding most affected area function here:by using above dictionary of affected areas count
def most_affected_area(areas_affected):
    
    max_area = " "
    max_count  = 0
    
    for x in affected_areas_count:
        if affected_areas_count[x] >  max_count:
            max_area = x
            max_count = affected_areas_count[x]
    return max_area, max_count
        
max_area, max_count = most_affected_area(areas_affected)
#print(max_area, max_count)
#print(f"Area: {max_area}, Count: {max_count}")

#Finding the highest mortality hurricane and the number of deaths it caused.
def highest_mortality(hurricanes): 
    hurricane_name = " "
    no_of_deaths = 0
    for x in hurricanes:
        if hurricanes[x]['Deaths'] > no_of_deaths:
            hurricane_name = x
            no_of_deaths = hurricanes[x]['Deaths']
    return hurricane_name, no_of_deaths

hurricane_name, no_of_deaths = highest_mortality(hurricanes)
print(hurricane_name, no_of_deaths)

# catgeorize by mortality function here:  return a dictionary with rates starting from 0 to 5 as keys and values 
#if deaths < 100, then assign values to keys(rates) , (check in hurricanes list)

def mortality(hurricanes):
    hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for x in hurricanes:
        rate = 0
        deaths = hurricanes[x]['Deaths'] 
        
        if deaths < 100:
            rate = 0
        elif deaths >= 100 and deaths < 500:
            rate = 1
        elif deaths >= 500 and deaths < 1000:
            rate = 2
        elif deaths >= 1000 and deaths < 10000:
            rate = 3
        else:
            rate = 4
            
        if rate not in hurricanes_by_mortality:
            hurricanes_by_mortality[rate] = hurricanes[x]
        else:
            hurricanes_by_mortality[rate].append(hurricanes[x])
            
    return hurricanes_by_mortality
    
#mortality_rates = mortality(hurricanes)
#print(mortality_rates)

#Greatest damage function  Function to find out the name of Hurricane and the greatest damage occured in hurricane dictionary
def greatest_damage(hurricanes):
        max_damage_hurricane = " "
        max_damage_number = 0
        
        for x in hurricanes:
            if hurricanes[x]['Damage'] == 'Damages not recorded':
                continue
            
            if hurricanes[x]['Damage'] > max_damage_number:
                max_damage_hurricane = hurricanes[x]['Name']
                max_damage_number = hurricanes[x]['Damage']
            
            return max_damage_hurricane, max_damage_number

max_damage_hurricane, max_damage_number = greatest_damage(hurricanes)
print(max_damage_hurricane, max_damage_number)

#catgeorize by damage function here:

def damage(hurricanes):
    damage_scale = {0:[],1:[],2:[],3:[],4:[]}
    for x in hurricanes:
        
        rate = 0
        damage = hurricanes[x]['Damage']
    
        if damage == 'Damages not recorded':
            continue
        elif damage < 100000000:
            rate = 0
        elif damage >= 100000000 and damage < 1000000000:
            rate = 1
        elif damage >= 1000000000 and damage < 10000000000:
            rate = 2
        elif damage >= 10000000000 and damage < 50000000000:
            rate = 3
        else:
            rate = 4

        if rate not in damage_scale:
            damage_scale[rate] = hurricanes[x]
        else:
            damage_scale[rate].append(hurricanes[x])

    return damage_scale    
    
    
print(damage(hurricanes))
    
    
    
    
    
