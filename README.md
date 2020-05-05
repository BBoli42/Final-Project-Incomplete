# Project Title
Belinda Bolivar
[Link to this repository]https://github.com/BBoli42/Final-Project-Checkin.git
---
## Project Description
This project should allow users to see a list of parks in a state. Additionally, they should be able to see well formatted webpages that allow them to click back and forth.

WEB SCRAPING
nat_park_soup contains code to scrape from the national parks website, the name, location, and description of parks in the United States. It then create a csv of the data.  

DB BUILDING

SI507project_tools contains code to create a SQLite db. It contains three tables with many to many relationships as  parks can be in multiple states and multiple states can have many parks.

FLASK ROUTES:
The first route will take you to the form ("http://localhost:5000")

One route will allow them to input a state (Route "http://localhost:5000/form1"), see a list of parks, and then add that park to a list. (original goal)
However, that does not work.

Another route was created to take the input and display the input ("http://localhost:5000/test") which also does not work.

Another route ("http://localhost:5000/park_added") was added to show the parks that were added. Also does not work.




## How to run
1. install all requirements with `pip install -r requirements.txt`
2.  Second, you should run nat_park_soup.py
3.  Third, you should run SI507project_tools.py
4. pop_db.py, should populate the database but is not functional.
## How to use
1.  Run nat_park_soup
2.  Run SI507project_tools
3.  When file is running go to localhost:5000
4. Navigate from the home screen to the first form
5. To find a park enter the location using abbreviations and it should show a list of parks within that state.

(Optional): Markdown syntax to include an screenshot/image: ![alt
text](image.jpg)
## Routes in this application
-  `/home` -> this is the home page
-  `/form1` -> this form should take a state as an input
-  `/park_added` -> this will show you a park that you added and will also give you a fun fact using JavaScript

## How to run tests
1.  First run SI507project_test.py
2.  Second (e.g. any other setup necessary)
3.  etc (e.g. run the specific test file)
NOTE: Need not have 3 steps, but should have as many as are appropriate!
## In this repository:
-  Final_project
-  SI507project_test.py
-  SI507project_tools.py
-  nat_park_soup.py
-  requirements.text
-  sample_park_cache.json
-  sample_national_parks.db
-  sample1_national_parks_info.csv
-  final_advanced_expiry_caching
-  templates
-  image of diagram
-  pop_db.py - does not work
- repository of failed files
---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as
demonstrated.
-  [ ] This is a completed requirement.
-  [ ] This is an incomplete requirement.
Below is a list of the requirements listed in the rubric for you to copy
and paste.  See rubric on Canvas for more details.
### General
-  [X ] Project is submitted as a Github repository
-  [X ] Project includes a working Flask application that runs locally on a
computer
-  [ X] Project includes at least 1 test suite file with reasonable tests
in it.
-  [ X] Includes a `requirements.txt` file containing all required modules
to run program
-  [X ] Includes a clear and readable README.md that follows this template
-  [ X] Includes EVERY file needed in order to run the project
-  [ X] Includes screenshots and/or clear descriptions of what your project
should look like when it is working
### Flask Application
-  [ X] Includes at least 3 different routes
-  [X ] View/s a user can see when the application runs that are a list of parks and a description
understandable/legible for someone who has NOT taken this course
-  [ ] Interactions with a database that has at least 2 tables
-  [X ] At least 1 relationship between 2 tables in database
-  [ ] Information stored in the database is viewed or interacted with in
some way
### Additional Components (at least 6 required)
-  [ ] Use of a new module
-  [ ] Use of a second new module
-  [ ] Object definitions using inheritance (indicate if this counts for 2
or 3 of the six requirements in a parenthetical)
-  [X] At least one form in your Flask application
-  [ ] Templating in your Flask application
-  [X] Inclusion of JavaScript files in the application
-  [X] Links in the views of Flask application page/s
-  [ ] Relevant use of `itertools` and/or `collections`
-  [X] Sourcing of data using web scraping
-  [X] Sourcing of data using web REST API requests
-  [X ] Sourcing of data using user input and/or a downloaded .csv or .json
dataset TO DO
-  [X] Caching of data you continually retrieve from the internet in some DONE
way
### Submission
-  [ ] I included a link to my GitHub repository with the correct
permissions on Canvas! (Did you though? Did you actually? Are you sure
you didn't forget?)
-  [ ] I included a summary of my project and how I thought it went **in
my Canvas submission**!
# Final-Project-Check-In
