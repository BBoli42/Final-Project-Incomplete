import requests, json
from bs4 import BeautifulSoup
from final_advanced_expiry_caching import Cache
import csv
# import sqlite3
###Right file
#####TO DO WRITE LINE OF CODE TO FEED LIST TO DATABASE / CREATE TUPLES
###MIGHT NEED TO CHANGE THINGS INTO OBJECTS

START_URL = "https://www.nps.gov/index.htm"
FILENAME = "sample_park_cache.json"

PROGRAM_CACHE = Cache(FILENAME)


def access_page_data(url):
    data = PROGRAM_CACHE.get(url)# get data from the url # get tool will return NONE if it doesn't exist
    if not data:
        data = requests.get(url).text # if data is not there put it there
        PROGRAM_CACHE.set(url, data)
    return data

#######
##what all the data from this webpage and all the info from the hyperlinks
main_page = access_page_data(START_URL) # all the data from the main page and it cache data


main_soup = BeautifulSoup(main_page, features="html.parser")#.encode("utf-8") #change
list_of_topics = main_soup.find('ul',{'class':'dropdown-menu SearchBar-keywordSearch'})  # should contain list of tags
# print(list_of_topics) # cool


all_links = list_of_topics.find_all('a')
# print(all_links)

#a variable with all the links

path = "https://www.nps.gov/"


# want an istance that represents all the links
# path = "https://www.nps.gov/"
topics_pages = []
for l in all_links:
    page_data = access_page_data(path + l['href']) # maybe add path?
    soup_of_page = BeautifulSoup(page_data, features="html.parser")#.encode("unicode-escape")
    # print(page_data)
    # print(soup_of_page)
    topics_pages.append(soup_of_page)
    # print(topics_pages)
##### CAT CODE
nowhere = []
everything = []
for allstuff in topics_pages:
    all_obj = allstuff.find("li",{"class":"clearfix"})

    thor = all_obj.text
    everything.append(thor)
    list_of_abvstate = all_obj.find_all("h4")
    # print(list_of_abvstate)
    guardians = []

    for loki in list_of_abvstate:
        guardians = loki.text.split(",")
    list_of_des = all_obj.find("p").text
    list_of_pnames = all_obj.find("h3").text
    list_of_lists = str(guardians) + list_of_des + list_of_pnames
    # print(list_of_lists)


    for rocket in guardians:
        if len(rocket) != 2:
            continue
    #
    #
    #     list_of_states = []
    #     for value in some_states.split():##This give state abb.
    #         if len(value) <= 2:
    #             # if value =1
    #             list_of_states.append(value)
        # print(type(rocket))
        # print(rocket)
        benatar = []
        benatar.append(list_of_pnames)
        benatar.append(list_of_des)
        benatar.append(rocket)
        nowhere.append(benatar)






with open("national_parks_info.csv","w", newline = "", encoding='UTF8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Name", "Description","States"])
    for starlord in nowhere:
        writer.writerow(starlord)

######## END OF CAT CODE

states = []

for a_state in topics_pages:
    kinda_list_of_states = a_state.find("h1", {"class":"page-title"})# this works but just need the state names
    state_names = kinda_list_of_states.text #<class 'bs4.element.Tag'> ##This works
    # print(type(state_names))
    # print(states)
    # states = []
    # for all_states in state_names:
    states.append(state_names)
        # all_stuff.append(all_states)
    # print(type(states))
    # print(states)

state_list = []
for state_elem in topics_pages:
    list_of_abv = state_elem.find_all("h4")
    for stuff in list_of_abv:
        some_states = stuff.text

        list_of_states = []
        for value in some_states.split():##This give state abb.
            if len(value) <= 2:
                # if value =1
                list_of_states.append(value)
                # print(list_of_states) #THIS KINDA WORKS
                # print(type(list_of_states))
                # another_st_list = []
                # def get_state_abv(list_of_states): #creating function to get only the abv of states
                #     for st_list in list_of_states:
                #         if len(st_list) == []:
                #             another_st_list.append(st_list)
                #         print(another_st_list)



#TYPE <h2>National Monument</h2
nat_park_types = []

for a_type in topics_pages:
    # print(a_type.find("h2")) #maybe not the right tag but getting close
    # soup_types = a_type.find("div", {"class":"col-md-9 col-sm-9 col-xs-12 table-cell list_left"})
    # kinda_list_of_types = soup_types("h2") # gets very close
    # print(type(kinda_list_of_types))
    soup_types = a_type.find("ul", {"id":"list_parks"})
    kinda_list_of_types = (soup_types.findChildren("h2"))
    # print(kinda_list_of_types)
    # print(type(kinda_list_of_types))



# for each_elem in range(len(kinda_list_of_types)):
#     print(kinda_list_of_types[0, each_elem])

# print(kinda_list_of_types)
    # nat_park_types = []
    for each_elem in kinda_list_of_types:
#     print(type(kinda_list_of_types))
        elem_types = each_elem.text# this get one type
        # print(elem_types)
        nat_park_types.append(elem_types)
        # all_stuff.append(elem_types)


    #     nat_park_types = []
    #     for some_park_types in elem_types:
    #         print(some_park_types)
    # #     print(type(kinda_list_of_types))
    #         # type_names = some_park_types
    #         nat_park_types.append(some_park_types)
        # print(nat_park_types)



#DESCRIPTION <p>
p_d = []
# new_pd = []

for a_description in topics_pages:
    # print(a_description.find("p")) #this works
    # print(a_description)
    # print(v)
    soup_descriptions = a_description.find("p")
    park_description = soup_descriptions ## works but still has a <p>
    # print(type(park_description))


    # p_d = []
    for each_d in park_description:
#     print(type(kinda_list_of_types))
        descrip = each_d
        p_d.append(descrip)

        # print(p_d)


        # for a_p_d in p_d:
        #     print(type(a_p_d))
            # print(a_p_d) ##THIS WORKS AND GETS ALL ELEMENTS
            # some_apd = a_p_d.text
            # new_pd.append(a_p_d)
            # print(type(new_pd))
            # print(some_apd)
#.split("\n'"))

        # print(type(elem_name))
        # print(p_d.slice())

names = [] #THIS WORKS AND CONTAINS ALL ELEMENTS
#NAME <h3><a href="/bicr/">Birmingham Civil Rights</a></h3>
for a_name in topics_pages:
    list_of_names = a_name.find("ul", {"id":"list_parks"})
    name_list=(list_of_names.findChildren("h3"))
    # print(list_of_names)

    # names = []
    for each_name in name_list:
#     print(type(kinda_list_of_types))
        elem_name = each_name.text
        names.append(elem_name)
        # all_stuff.append(elem_name)
        # print(names)

        # print(kinda_list_of_types[0, each_elem])
    # writer.writerow([nat_park_types,names, p_d, elem_types])
    # for name_stuff in names:
        # for each_pd in p_d:
            # for each_types in nat_park_types:
        # print(name_stuff)


####Work Space
















































####End of Work Space




























# print(all_stuff)

#
# with open("national_parks_info.csv","w", newline = "", encoding='UTF8') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(["Name", "Description","States"])
#     for name in names:
#         # for des in p_d:
#         # print(name)
#             writer.writerow([name, p_d, list_of_states])
#
#
# with open("national_parks_des.csv","w", newline = "", encoding='UTF8') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(["Name", "Description","States"])
#     for des in p_d:
#         # for scrip in des:
#         # for des in p_d:
#         # print(name)
#             writer.writerow([names, des, list_of_states])
#
#     with open("national_parks_state.csv","w", newline = "", encoding='UTF8') as csv_file:
#         writer = csv.writer(csv_file)
#         writer.writerow(["Name", "Description","States"])
#     # print(list_of_states)
#         for state_thing in list_of_states:
#             print(list_of_states)
#         # for estate in state_thing:
#         # for scrip in des:
#         # for des in p_d:
#         # print(name)
#             writer.writerow([names, des, state_thing])

####IGNORE STUFF BELLOW



####Code not working
###code kinda works but needs more
# with open("national_parks_info.csv","w", newline = "", encoding='UTF8') as csv_file:
#     writer = csv.writer(csv_file)
#     # writer.writerow(["Name", "State", "Description", "Type"])
#     writer.writerow(["Name", "Description","States"])
#
#     for every_name in range(len(names)):
#         if every_name > len(p_d)-1:
#             break
#         elif every_name > len(list_of_states)-1:
#             writer.writerow([names[every_name],p_d[every_name],list_of_states[every_name]])
###Code doesn't work
#
# with open("national_parks_info.csv","w", newline = "", encoding='UTF8') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(["Name", "State", "Description"])
#     for thing in range(len(names)):
#         if thing > len(names)-1:
#             break
#     writer.writerow([names[thing],p_d[thing]])

    #     if thing
    #
    # for each_thing in all_things:
    #     # print(each_thing)
    #
    #
    #     # if thing not in all_things:
    #     #     thing = "na"
    #     # else:
    #     #     print(thing[all_things])
    # #     if state_des in p_d:
    # #         # print(state_des)
    # #         if many_state in list_of_states:
    #     writer.writerow(each_thing)
###Code###


# with open("national_parks_state.csv","w", newline = "", encoding='UTF8') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(["State"])
#     for stuff in range(len(list_of_states)):
#         print(stuff)
#     # if an_item not in stuff:
#         writer.writerow(stuff[list_of_states])

        # print(stuff[list_of_states])
    #     for allstuff in stuff:
    #         print(allstuff)
        # writer.writerow(stuff[list_of_states])
###Code
# with open("national_parks_info.csv","w", newline = "", encoding='UTF8') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow)(["Name", "State", "Description"])
#     for name_st in range(len(names)):
#         if name_st not < p_d:
#     writer.writerow([names, p_d])
    # list_of_states])


###Code 1/
#all_things = [names,list_of_states, p_d]
# for each_thing in all_things:
#     pass
#     return each_thing
# with open("national_parks_info.csv","w", newline = "", encoding='UTF8') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(["Name", "State", "Description"])
#     for thing in range(len(all_things)):
#     #     if thing
#
#     # for each_thing in all_things:
#         # print(each_thing)
#
#
#         # if thing not in all_things:
#         #     thing = "na"
#         # else:
#         #     print(thing[all_things])
#     #     if state_des in p_d:
#     #         # print(state_des)
#     #         if many_state in list_of_states:
#         writer.writerow([all_things])
####Code 2

# with open("national_parks_info.csv","w", newline = "", encoding='UTF8') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(["Name", "State", "Description"])
#     for name in range(len(names)):
#         if state_des in p_d:
#             # print(state_des)
#             if many_state in list_of_states:
#                 writer.writerow(name, state_des, many_state)


###Code
# with open("national_parks_info.csv","w", newline = "", encoding='UTF8') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(["Name", "State", "Description"])
#     for name in names:
#         if name
#         writer.writerow([names[name_stuff], list_of_states[name_stuff], p_d[name_stuff]])
    # for each_name in names:
    #     writer.writerow([names[each_name],list_of_states[each_name],p_d[each_name]])



###Code

# with open("national_parks_info.csv","w", newline = "", encoding='UTF8') as csv_file:
#     writer = csv.writer(csv_file)
#     # writer.writerow(["Name", "State", "Description", "Type"])
#     writer.writerow(["Name", "Description"])#, "Location"])
###Code

# with open("national_parks_info.csv","w", newline = "", encoding='UTF8') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(["Name", "State", "Description"])
#     for each_name in names:
#         if each_name > len(nat_park_types)-1:
#             break
#         writer.writerow([names[each_name],nat_park_types[each_name]])
        # if each_name
        # print(each_name)
        # writer.writerow([each_name])

###Code

# with open("des_national_parks_info.csv","w", newline = "", encoding='UTF8') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(["Name", "State", "Description"])
#     for each_type in nat_park_types:
#         # if each_name
#         # print(each_dlist)
#         writer.writerow([each_type])
        #
        # writer.writerow([each_npt],list_of_states[each_npt], p_d[each_npt])
    # for each_dlist in p_d:
    #     print(each_dlist)
    #     writer.writerow([each_npt],list_of_states[each_npt], each_dlist[each_npt])

###Code

# with open("test_national_parks_info.csv","w", newline = "", encoding='UTF8') as csv_file:
#     writer = csv.writer(csv_file)
#     # writer.writerow(["Name", "State", "Description", "Type"])
#     writer.writerow(["Name", "Description"])
#
#     for every_name in range(len(names)):
#         if every_name > len(p_d)-1:
#             pass
#         if every_name < len(list_of_states)-1:
#             pass
#         writer.writerow([names[every_name],p_d[every_name],list_of_states[every_name]])



        # print(kinda_list_of_types[0, each_elem])
    # writer.writerow([nat_park_types,names, p_d, elem_types])
    # for name_stuff in names:
    #     # for each_pd in p_d:
    #         # for each_types in nat_park_types:
    #     print(name_stuff)
    # for name_stuff in range(len(names)):
    #     if name_stuff != p_d:
    #         name_stuff = "n/a"
    #     else:
#         writer.writerow([names[name_stuff], list_of_states[name_stuff], p_d[name_stuff]])#,


###Don't delete
#     for every_name in range(len(names)):
#         if every_name > len(p_d)-1:
#             break
# #         elif every_name < len(p_d)-1:
# #             # every_name = "na"
# #
# #             # if every_name > len(list_of_states-1):
# #             #     break
#             writer.writerow([names[every_name],p_d[every_name]])#, list_of_states[every_name]])
