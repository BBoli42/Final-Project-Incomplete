import requests, json
from bs4 import BeautifulSoup
from final_advanced_expiry_caching import Cache
import csv
# import sqlite3

#####TO DO WRITE LINE OF CODE TO FEED LIST TO DATABASE / CREATE TUPLES
###MIGHT NEED TO CHANGE THINGS INTO OBJECTS

START_URL = "https://www.nps.gov/index.htm"
FILENAME = "sample_park_cache.json"
# url = "https://www.nps.gov/index.htm"
# So I can use 1 (one) instance of the Cache tool -- just one for my whole program, even though I'll get data from multiple places
PROGRAM_CACHE = Cache(FILENAME)# kind of a constance, creating an instance where ammendments could be made


def access_page_data(url):
    data = PROGRAM_CACHE.get(url)# get data from the url # get tool will return NONE if it doesn't exist
    if not data:
        data = requests.get(url).text # if data is not there put it there
        PROGRAM_CACHE.set(url, data) # default here with the Cache.set tool is that it will expire in 7 days, which is probs fine, but something to explore # first put identifier and then what data is associated with the url
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
# for link in all_links:
#     print(path + link['href'])
#add url to links somehow

# want an istance that represents all the links
# path = "https://www.nps.gov/"
topics_pages = [] # gotta get all the data in BeautifulSoup objects to work with...
for l in all_links:
    page_data = access_page_data(path + l['href']) # maybe add path?
    soup_of_page = BeautifulSoup(page_data, features="html.parser")#.encode("unicode-escape")
    # print(page_data)
    # print(soup_of_page)
    topics_pages.append(soup_of_page)
    # print(topics_pages)

#Error:  MissingSchema(error) requests.exceptions.MissingSchema: Invalid URL '/state/al/index.htm': No schemasupplied. Perhaps you meant http:///state/al/index.htm?
#Solution: the error is in the requests part of the code. Add a line/path so that a url can be created and scrapped.

# for something in topics_pages:
#     print(something)

# print(topics_pages[0].prettify())
# print(type(topics_pages))# this is a list of beautifulsoup objects

# all_stuff = []
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
    # for each_state in states:
    #     print(each_state)
    # states = []
    # for names_of_states in state_names:
    #     states.append(names_of_states)
    # print(states)

state_list = []
for state_elem in topics_pages:
    list_of_abv = state_elem.find_all("h4")
    for stuff in list_of_abv:
        some_states = stuff.text
        # print(type(some_states))
        # print(len(some_states.split()))
        # print(some_states.split())
        list_of_states = []
        for value in some_states.split():
            if len(value) <= 2:
                # if value =1
                list_of_states.append(value)
                # print(list_of_states) #THIS KINDA WORKS
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
    soup_descriptions = a_description.find("p")
    park_description = soup_descriptions ## works but still has a <p>
    # print(type(park_description))


    # p_d = []
    for each_d in park_description:
#     print(type(kinda_list_of_types))
        descrip = each_d
        p_d.append(descrip)
        # print(p_d.ascii())
        # p_d.append(descrip.split('\''))
        # all_stuff.append(descrip)
        # p_des = []
        # for each_des in p_d:
        #     a_des = (str(each_des))
        #     # print(type(a_des))
        #     print(a_des.split(","))
            # p_des.append(a_des)
            # print(a_des.split())
            # p_des.append(each_des)
            # print(p_des)

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

def get_park_info():
    for item in get_park_info:
        print(item)
    get_park_info(names)

###WRITING INTO A CSV FILE
# with open("national_parks_info.csv","w", newline = "", encoding='UTF8') as csv_file:
#     writer = csv.writer(csv_file)
# #     # writer.writerow(["Name", "State", "Description", "Type"])
#     writer.writerow(["Name", "State,""Description"])
# #
#     for every_name in range(len(names)):
#         if every_name not in range(len(names)):
#             every_name = " n/a"
#         else:
#
#         # if every_name > len(p_d)-1:
#         #     break
#             writer.writerow([names[every_name],p_d[every_name], list_of_states[every_name]])


# with open("national_parks_info.csv","w", newline = "", encoding='UTF8') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(["Name", "State", "Description"])
#     for each_npt in nat_park_types:
#         print(each_npt)
#         writer.writerow([each_npt])




        # print(kinda_list_of_types[0, each_elem])
    # writer.writerow([nat_park_types,names, p_d, elem_types])
    for name_stuff in names:
        # for each_pd in p_d:
            # for each_types in nat_park_types:
        print(name_stuff)
    # for name_stuff in range(len(names)):
    #     if name_stuff != p_d:
    #         name_stuff = "n/a"
    #     else:
    #         writer.writerow([names[name_stuff], list_of_states[name_stuff], p_d[name_stuff]])#, nat_park_types])


        # if name_stuff in names > pd:
        #     name_stuff = "n/a"
        # else:
        #     print(name_stuff)
    # writer.writerow([names[name_stuff], list_of_states[name_stuff], p_d[name_stuff]])#, nat_park_types])

                # writer.writerow([name_stuff, list_of_states, p_d])#, nat_park_types])

            # writer.writerow([name_stuff, list_of_states, p_d])#, nat_park_types])
        # for each_pd in p_d:
        #     writer.writerow([name_stuff, states, p_d, nat_park_types])
        #
        #     for each_types in nat_park_types:
        #         writer.writerow([name_stuff, states, p_d, nat_park_types])



    # for state_names, elem_type, descrip, elem_name in all_stuff:
    #     writer.writerow([state_names,elem_type, descrip, elem_name])


    # for each_national_park in nat_park_types:
    #     print(each_national_park)
        # for a_park in each_national_park:
        #     print(a_park)
        # for every_name in names:
        #     print(every_name)


    # for each_descrip in p_d:
        # print(each_descrip)
        # writer.writerow([name_stuff, states, p_d, nat_park_types])

    # for every_state in state_names:
    #     print(every_state)



        # writer.writerow([name_stuff, states, p_d, nat_park_types])

# with open('some.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerows(zip(states, nat_park_types, p_d, names ))
# #DID NOT WORK
# rows = zip(states, nat_park_types, p_d, names)
# with open("nat_parks.csv", "w") as f:
#     writer = csv.writer(f)
#     for row in rows:
#         writer.writerow(row)
#can write things into this file
# a_file = open("info_about_parks.csv", "w")
# a_file.write("Name,Type,Description, Location")
# a_file.write([state_names, park_description, elem_name, elem_types])
# # a_file.write([names, states, p_d, nat_park_types])
#
# a_file.write("\n")
