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

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def convert_M_B(damage):
    convertion = []
    for i in damage:
        if 'M' in i:
            convertion.append(float(i[:-1]) * 1000000)
        elif 'B' in i:
            convertion.append(float(i[:-2]) * 1000000000)
        elif 'Damages not recorded' == i:
            convertion.append(i)
    return convertion

damages_converted = convert_M_B(damages)
#print(damages_converted)


# write your construct hurricane dictionary function here:
def create_database(a, b, c, d, e, f, g):
    database = {}
    for i in range(len(names)):
        database[names[i]] = {'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damage': damages_converted[i],
                       'Deaths': deaths[i]}
    return database

database = create_database(names, months, years, max_sustained_winds, areas_affected, damages_converted, deaths)



# write your construct hurricane by year dictionary function here:

def year_dictionary_funtion(database):

    unique_years = []
    database_years = {}

    for i in range(len(database)):
        if list(list(database.values())[i].values())[2] not in unique_years:
            unique_years.append(list(list(database.values())[i].values())[2])
            database_years[list(list(database.values())[i].values())[2]] = [list(database.values())[i]]
        elif list(list(database.values())[i].values())[2] in unique_years:
           database_years[list(list(database.values())[i].values())[2]].append(list(database.values())[i])
    return database_years

#print(unique_years)
#print(year_dictionary_funtion(database))

# write your count affected areas function here:

def dict_affect_area(areas_affected):
    count_dict = {}
    unique_area = []

    for area in areas_affected:
        for a in area:
            if a not in unique_area:
                unique_area.append(a)

    unique_area = sorted(unique_area)
    #print(len(unique_area))

    for area in range(len(unique_area)):
        count = 0
        for a in areas_affected:
            if unique_area[area] in a:
                count += 1
            count_dict[unique_area[area]] = count

    return count_dict


dict_affect = dict_affect_area(areas_affected)


# write your find most affected area function here:
def most_affected_area(dict_affect):
    highest = 0
    area = ''
    for k, v in dict_affect.items():
        if v > highest:
            highest = v
            area = k

    return 'The most affected area is {area} with {highest} hurricanes.'.format(area=area, highest=highest)

#print(most_affected_area(dict_affect))


# write your greatest number of deaths function here:

def hurricane_v_deaths(names, deaths):

    hurricanes_deaths = {h: d for h, d in zip(names, deaths)}
    highest = 0
    hurricane = ''
    for k, v in hurricanes_deaths.items():
        if v > highest:
            highest = v
            hurricane = k

    return hurricane, highest

#print(hurricane_v_deaths(names, deaths))

# write your catgeorize by mortality function here:

mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def categorized(names, deaths, mortality_scale):

    hurricane_deaths_dict = {h: d for h, d in zip(names, deaths)}

    list_0 = []
    list_1 = []
    list_2 = []
    list_3 = []
    list_4 = []
    list_5 = []

    for k ,v in hurricane_deaths_dict.items():
        try:
            if v > list(mortality_scale.values())[4]:
                list_5.append(k)
            elif v > list(mortality_scale.values())[3]:
                list_4.append(k)
            elif v > list(mortality_scale.values())[2]:
                list_3.append(k)
            elif v > list(mortality_scale.values())[1]:
                list_2.append(k)
            elif v > list(mortality_scale.values())[0]:
                list_1.append(k)
            elif v == list(mortality_scale.values())[0]:
                list_0.append(k)
        except:
            continue

    total_list = [list_0] + [list_1] + [list_2] + [list_3] + [list_4]

    scale_keys = []

    for k in mortality_scale.keys():
        scale_keys.append(k)

    final_scale = {k: v for k, v in zip(scale_keys, total_list)}

    return final_scale

# write your greatest damage function here:

def greatest_damage_function(names, damages):
    names_damage = {n: d for n, d in zip(names, damages)}

    top_damage_hurricane = ''
    highest_damage = 0

    for k, v in names_damage.items():
        try:
            if v > highest_damage:
                highest_damage = v
                top_damage_hurricane = k
        except:
            continue

    return top_damage_hurricane, highest_damage

print(greatest_damage_function(names, damages_converted))


# write your catgeorize by damage function here:
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

#Used same function as in task# 8

#print(categorized(names, damages_converted, damage_scale))


