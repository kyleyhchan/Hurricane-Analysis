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
def MB_to_num(li):
    conversion = {"M": 1000000, "B": 1000000000}
    new_list = []
    for i in li:
        if i[-1] == "M":
            new_list.append(int(float(i[:-1])*conversion["M"]))
        elif i[-1] == "B":
            new_list.append(int(float(i[:-1])*conversion["B"]))

        else:
            new_list.append(i)
    return new_list


update_damages = MB_to_num(damages)
print(type(update_damages[1]))



# write your construct hurricane dictionary function here:
def dict_construct(name):
    new_dict = {}
    for i in range(len(names)):
        new_dict[name[i]]={'Name':name[i],'Month':months[i],'Year':years[i],'Max Sustained Wind': max_sustained_winds[i],'Areas Affected':areas_affected[i],'Damage':damages[i],"Death":deaths[i]}
    return new_dict






# write your construct hurricane by year dictionary function here:

def dict_construct_year(hh):
    new_dict = {}
 

    for i in hh:
        current_year = hh[i]["Year"]
        current_cane = hh[i]

       
        if current_year in new_dict:
            new_dict[current_year].append(current_cane)
        else:
            new_dict[current_year]=[current_cane]
        
    return new_dict


hurricane = dict_construct(names)


hurricane_by_year = dict_construct_year(hurricane)
 



# write your count affected areas function here:
def afftected_area_count(area):
    new_dict = {}
    for i in area:
        for j in i:
            if j in new_dict:
                new_dict[j] += 1
            else:
                new_dict[j] = 1

    return new_dict

areas_count = afftected_area_count(areas_affected)





# write your find most affected area function here:
def most_affected_area(area_count):
    count_list = list(area_count.values())
   
    name_list = list(area_count.keys())
   
    num = count_list.index(max(count_list))
    most_area = name_list[num]

    
    return most_area
    





# write your greatest number of deaths function here:
def most_death(death):
    num_index = deaths.index(max(deaths))
    string = names[num_index] + ": " +str(deaths[num_index])
    return string


print(most_death(deaths))







# write your catgeorize by mortality function here:
def morality():
    mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
    hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for i in range(len(names)):
        if deaths[i] >0 and deaths[i] <= 100:
            hurricanes_by_mortality[1].append(names[i])
        elif deaths[i] >100 and deaths[i] <= 500:
            hurricanes_by_mortality[2].append(names[i])
        elif deaths[i] >500 and deaths[i] <= 100:
            hurricanes_by_mortality[3].append(names[i])
        elif deaths[i] >1000 and deaths[i] <= 10000:
            hurricanes_by_mortality[4].append(names[i])
        elif deaths[i] >10000:
            hurricanes_by_mortality[5].append(names[i])
        else:
            hurricanes_by_mortality[0].append(names[i])

    return hurricanes_by_mortality








# write your greatest damage function here:
def most_damage_cost():
    update_damages = MB_to_num(damages)
    name_list = []
    damage_list = []
    for i in range(len(names)):
        name = names[i]
        damage = update_damages[i]

        if isinstance(damage, int) == True:
            name_list.append(names[i])
            damage_list.append(update_damages[i])
    most_damage = name_list[damage_list.index(max(damage_list))]
    return most_damage

print(most_damage_cost())





# write your catgeorize by damage function here:
