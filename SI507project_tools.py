from flask import Flask
from flask import Flask, request, render_template, session, redirect, url_for


import os
from flask import Flask, request, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import nat_park_soup
import requests




app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./sample_national_parks.db' #creates database
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

#Creates tables

associations = db.Table('National_Parks',db.Column('location_id',db.Integer, db.ForeignKey('location.id')),db.Column('parks_id',db.Integer, db.ForeignKey('parks.id')))


class Location(db.Model):
    __tablename__ = "location"
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(64))
    # park = relationship ("")
    park = db.relationship('Parks',secondary='National_Parks',backref=db.backref('location',lazy='dynamic'),lazy='dynamic')
    # park = db.relationship('Parks',secondary=associations,backref=db.backref('location',lazy='dynamic'),lazy='dynamic')

    # parks = db.relationship('Parks',backref='Location')

# class Description(db.Model):
#     __tablename__="parks"
#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.String(250))

class Parks(db.Model):
    __tablename__="parks"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    state = db.Column(db.String(64))
    # type = db.Column(db.String(64))
    description = db.Column(db.String(250))
    # location = db.relationship('Location',secondary='National_Parks',backref=db.backref('parks',lazy='dynamic'),lazy='dynamic')
    db.relationship('Location',secondary=associations,backref=db.backref('parks',lazy='dynamic'),lazy='dynamic')
    # parks = db.relationship('National_Parks',backref='Parks')


    def __repr__(self):
        return "{} is in {} and is a {}.".format(self.parkname,self.location, self.type)

def get_a_state(some_states):
    park_locations = Location.query.filter_by(state=some_states)
    if park_locations:
        return park_locations
    else:
        park_locations = Location(state=some_states)
        session.add(park_locations)
        session.commit()
        return park_locations
# Set up application
# app = Flask(__name__)

###SETTING UP ROUTES
## Main route

####Change to 3rd Route
#Will interact and save info about states

# @app.route('/')
# def home():
#     pass #

# # ##MAIN ROUTE/HOMEPAGE
@app.route('/')
def parks_index():
    # titles = Title.query.all() #change
    # num_titles = len(titles) # change
    # return "hello"
    return '<h1> This is the main page! Want to know about national parks? </h1>. <a href="http://localhost:5000/form1">Click here to get started.</a>'
#
    # return render_template('parks_index.html', 'This is the main page. <a href="http://localhost:5000/form1">Click here to see the form.</a>')
#     # return render_template('test.html')
#
# ###FORM ROUTE
@app.route('/form1',methods=["GET", "POST"])

def form1():
    #  """ <form action="http://localhost:5000/result" method='GET'>
    # <form>
    # <h>Enter in name of a state</h>
    #   <input type="text" name="state">
    #
    #    <button type="button" onclick="alert('Input Saved')">Save</button>
    #
    #  </form>"""

# Does not work:
    # if request.method == "POST":
    #     user = request.form["state"]
    #     return redirect("http://localhost:5000/test" ("user", test=user ))
    # else:
#Does not work.
     return render_template('parks_index.html')

    # return '<h1>National Parks List</h1><h1>Add a park</h1> <h1>Please enter a state</h1>'

#Does not work:
@app.route('/test', methods = ["POST"])

def display_additions():
    name = request.form["name"]
    nofp = request.form["nofp"]

    # if request.method=='GET':
    #     return "You added"  + nofp + "and" + name +"is the location."
    # elif request.method=='POST':
    #         return "did it work?"
#Does not work.


@app.route('/park_added')

def park_added():

    # return "<button type="button""

    return render_template('savedname.html')

    # '<h1> Thank you. This park has been added. Please return to the previous page to add another park. </h1>. <a href="http://localhost:5000/form1">Previous.</a>'



####RESULTS ROUTE

# @app.route('/result', methods= ["GET"])
# def result_form1():
#     return "Here are the results for the state you selected!"
#     if request.method == "GET":
#         print(request.args)
#         if len(request.args)>0: ##tests Length of arg
#             for k in request.args:
#                 park_type = request.args.get(k, "None")
#                 park = Parks.query.filter_by(type=park_type).first() #an instance?
#                 if not park:
#                     park = Parks(type=reuqest.args.get(k, "None"), number_owned=0)
#                     session.add(park)
#                     session.commit()
#                 return "Does this work?"










#Below is okay DON'T DELETE

if __name__ == '__main__':
    # db.create_all()
    app.run()

####For CSV DON'T DELETE
# print("__name__:" + __name__)
# if __name__ == '__main__':
#     db.create_all()
#     pop_db.main_populate("national_parks_info.csv")
# app.run()
