import os
from flask import Flask, request, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import nat_park_soup
import requests




app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./sample_national_parks.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)



associations = db.Table('National_Parks',db.Column('location_id',db.Integer, db.ForeignKey('location.id')),db.Column('parks_id',db.Integer, db.ForeignKey('parks.id')))


class Location(db.Model):
    __tablename__ = "location"
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(64))
    # parks = db.relationship('Type',secondary=associations,backref=db.backref('location',lazy='dynamic'),lazy='dynamic')
    parks = db.relationship('Parks',backref='Location')


class Parks(db.Model):
    __tablename__="parks"
    id = db.Column(db.Integer, primary_key=True)
    parkname = db.Column(db.String(64))
    type = db.Column(db.String(64))
    description = db.Column(db.String(250))
    location = db.relationship('Location',secondary=associations,backref=db.backref('parks',lazy='dynamic'),lazy='dynamic')
    parks = db.relationship('Location',backref='Parks')


    def __repr__(self):
        return "{} is in {}.".format(self.parkname,self.location)

# meta = MetaData(engine)
# state = Location(state_list)
# session.add(state)
# print(state.id)
# ins = associations.insert().values(state="MI")
# conn = engine.connect()
# conn.execute(ins)
###HELPER FUNCTION

# def get_type(type_name):
#     type = Type.query.filter_by(parktype=type_name).first()
#     if type:
#         return type
#     else:
#         type = Type(parktype=type_name)
#         session.add(type)
#         session.commit()
#         return type
# def get_park(park_name):
#     park = Parks.query.filter_by(park_name = type_name).first()
#     if park:
#         return park
#     else:
#         park = Parks(park_name = type_name)
#         session.add(parks)
#         session.commit()
#         return park


#
# def get_name(names):
#     p_n = Parks.query.filter_by(names=parkname).first()
#     if p_n:
#         return p_n
#     else:
#         p_n = Parks(names=parkname)
#         session.add(p_n)
#         session.commit()
#         return p_n
def get_a_state(some_states):
    park_locations = Location.query.filter_by(state=some_states)
    if park_locations:
        return park_locations
    else:
        park_locations = Location(state=some_states)
        session.add(park_locations)
        session.commit()
        return park_locations


###SETTING UP ROUTES
## Main route

####Change to 3rd Route
#Will interact and save info about states
@app.route('/')
def parks_index():
    # titles = Title.query.all() #change
    # num_titles = len(titles) # change
    # return "hello"
    return 'This is the main page. <a href="http://localhost:5000/form1">Click here to get started.</a>'

    # return render_template('parks_index.html', 'This is the main page. <a href="http://localhost:5000/form1">Click here to see the form.</a>')
    # return render_template('test.html')

@app.route('/form1')
def form1():
    return """ <form action="http://localhost:5000/result" method='GET'>
    <form>
    <h>Enter in name of a state</h>
      <input type="text" name="state">

       <button type="button" onclick="alert('Input Saved')">Save</button>

     </form>"""
    # # render_template('parks_index.html')
# WANT TO INTERACT WITH A DATABASE

###needed but not sure where to put it 
def user_input(x):
    x.lowercase()


@app.route('/result', methods=["GET"])
def result_form1():
    if request.method == "GET":
        print(request.args)
        if len(request.args)> 0:
            for k in request.args:
                st_park = request.args.get(k, "None")
                states_in_park = Parks.query.filter_by(type = st_park).first()
                if not states_in_park:
                    states_in_park = Parks(type = request.args.get(k,"None"), state = 0)
                    session.add(states_in_park)
                    session.commit()
                states_in_park.state += 1
                session.add(states_in_park)
                session.commit()
            return "This works. <br><br> <a href='http://localhost:5000/'>Go to the main page</a>"





@app.route('/form_descrip')
def form_descrip():
    return render_template('description_of_park.html')
# #WANT TO INTERACT WITH A DATABASE
#
@app.route('/result2', methods=["GET"])
def park_descrip():
    return '''html>head<title>Hello</title><head><body><h1><Hello</h></body></html>'''







# @app.route('/')
# def parks_index():
#     # titles = Title.query.all() #change
#     # num_titles = len(titles) # change
#     # return "hello"
#     return render_template('parks_index.html')
#More routes
####
##Create routes that interact with another database: This will
####





####Form Examples


# @app.route('/')
# def hello_world():
#     return 'This is the main page. <a href="http://localhost:5000/form1">Click here to see the form.</a>'

# @app.route('/form1')
# def form1():
#     return """ <form action="http://localhost:5000/result" method='GET'>
#   <input type="checkbox" name="vehicle1" value="Bike"> I have a bike<br>
#   <input type = "checkbox" name"vehicle4" value = "Magic carpet"> I have a magic carpet<br>
#   <input type="checkbox" name="vehicle2" value="Car"> I have a car<br>
#   <input type="checkbox" name="vehicle3" value="Trolley"> I have a trolley
#   <input type="submit" value="Submit">
# </form>""" # You can imagine that you could also put this HTML in a form -- there are actually Flask-y libraries that help you use forms more efficiently, but for now we want to look at the simplest possible version to understand what's going on
#
# @app.route('/result',methods=["GET"])
# def result_form1():
#     if request.method == "GET":
#         print(request.args) # Check out your Terminal window where you're running this...
#         result_str = ""
#         for k in request.args:
#             result_str += "{} - {}<br><br>".format(k, request.args.get(k,""))
#         return result_str
#     return "Nothing was selected this time!"


#####
# @app.route('/add/new/<parkname>/')
# def new_park(parkname):#,new,state):
#     if Parks.query.filter_by(parkname= parkname).first():
#         return "You have already add that park.Please add another!"
#     else:
#         type = get_type(type)
#         # movie= Title(movie_title=movie_title, genre_id=name.id,language=language)#FIX
#         # movie= Title(movie_title=movie_title, genre_id=genre.id,language=language)#FIX
#         a_park = Parks(parkname = parkname)
#         session.add(movie) #FIX
#         session.commit()

#####EXAMPLE ROUTES
#
# #Set up more routes
#
# @app.route('/movie/new/<movie_title>/<genre>/<language>/')
# def new_title(movie_title,genre, language):
#     if Title.query.filter_by(movie_title=movie_title).first():
#         return "That movie already exists! Go back to the main app!"
#     else:
#         genre = get_genre(genre)
#         # movie= Title(movie_title=movie_title, genre_id=name.id,language=language)#FIX
#         movie= Title(movie_title=movie_title, genre_id=genre.id,language=language)#FIX
#         session.add(movie) #FIX
#         session.commit()
#         return "New movie: is called {} and is a {}. Check out the URL for ALL movies to see the whole list.".format(movie.movie_title, genre.name)
#

# def list_of_d():
#     if request.form:
#         book = Description(title=request.form.get("title"))
#         db.session.add(book)
#         db.session.commit()
#     return render_template("description.html")

# def list_of_parks():
#     if request.form:
#         book = Description(title=request.form.get("title"))
#         db.session.add(book)
#         db.session.commit()
#     return render_template("description_of_park.html")

# @app.route('/all_movies')
# def see_all():
#     all_movies = []
#     titles = Title.query.all()
#     for t in titles:
#         genre = Genre.query.filter_by(id=t.genre_id).first()
#         all_movies.append((t.movie_title,genre.name, t.language))#FIX
#     return render_template('all_movies.html', all_movies=all_movies)
# #
# #
# #
# @app.route('/all_genres')
# def see_all_genres():
#     genres = Genre.query.all()
#     names = []
#     for g in genres:
#         num_titles = len(Title.query.filter_by(genre_id=g.id).all())
#         newtup = (g.name,num_titles)
#         names.append(newtup) # names will be a list of tuples
#     return render_template('all_genres.html',genre_names=names)





#Below is okay

if __name__ == '__main__':
    db.create_all()
app.run()
