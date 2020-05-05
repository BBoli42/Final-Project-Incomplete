from just_flask import Parks, Location, session
# import SI507project_tools
# from just_alchemy import Parks, Location
import csv

def get_or_create_park(park_type_str):
    parks = Parks.query.filter_by(park_type_str).first()# check to see if it is there
    if not parks:
        parks = Parks(name = park_info_str)
        session.add(parks)
        session.commit()
    return parks

def get_or_create_location(park_location):
    location = Location.query.filter_by(name = park_location).first()
    if not location:
        location= Location(name = park_location)
        session.add(location)
        session.commit()
    return location

def get_or_create_natpark(park_data_dictionary):

    park = Parks.query.filter_by(parkname=park_data_dictionary["Parks"], state =True if park_data_dictionary["Location"]=="Parks" else False).first()

    #description= park_data_dictionary["Description"],state = park_data_dictionary["Location"]

    if not park:

        a_parks = get_or_create_car_park(park_data_dictionary["Parks"])
        location = get_or_create_location(park_data_dictionary["Location"])

        park = Parks.query.filter_by(parkname=park_data_dictionary["Park"], state =True if park_data_dictionary["Location"]=="Parks" else False).first()


        session.add(park)
        session.commit()

    return park


def main_populate(sample1_national_parks_info):
    print("here")
    try:
        with open(national_parks_info, newline="\n") as csvfile:
            print(csvfile)
            reader = csv.DictReader(csvfile)
            print(reader)
            for ln in reader:
                # print(ln)
                get_or_create_park(ln)
    # except Exception as e:
    except:
        # print(e)
        return False

# print("V")

if __name__ == "__main__":
    pass
