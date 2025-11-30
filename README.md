# INF601 - Advanced Programming in Python

# Jade Dofat

# Mini Project 4
 
## Description

This project uses django to let students
search for entry level jobs. The Internship Finder
allows users to browse internships and view job details.
There is also a log in option and a Django admin panel
for managing internship entries and uses Bootstrap and a modal.
The POST and GET routes support the search submissions.

# The pages:

The Home Page: a starting point with navigation to all main features

The Search Page: 
allows users to enter keywords and search internships

Details Page: shows information about a selected internship

the Saved Page: Users can save opportunities once 
they are logged in

The Login/Register Page: users 
access their accounts

the Admin Page: site admin can manage internship 
listings and user data

### Dependencies
 
This project requires:
-Python 3
-Django
-requirements.txt
-SQLite3
-Bootstrap

---> To ensure necessary packages are installed, create and activate
a virtual environment, then run pip install -r requirements.txt
before running the development server.

 
### Installing

Database Setup Commands

Clone the Repository:
- git clone https://github.com/jdofat/MiniProject4JadeDofat.git
- cd JadeDofatMiniProject4

1. create and activate venv:
   python3 -m venv venv
   source venv/bin/activate
   
2. install dependencies:
   pip install -r requirements.txt

3. run django migrations:
   python manage.py makemigrations
   python manage.py migrate

5. create django admin:
   python manage.py createsuperuser

6. run the development server:
   python manage.py runserver

 
## Authors
 
Jade Dofat

------

## Rubric

(5/5 points) Initial comments with your name, class and project at the top of your .py file.

(5/5 points) Proper import of packages used.

(70/70 points) Using Django you need to setup the following:

(10/10 points) Setup a proper folder structure, use the tutorial as an example. You need a minimum of one app.

(20/20 points) You need to have a minimum of 5 pages, using a proper template structure.

(10/10 points) You need to have at least one page that utilizes a form.

(10/10 points) You need to setup Django admin and style your models for proper entry. No tight restrictions here, just make use of the admin system.

(10/10) You need to use Bootstrap in your web templates. I won't dictate exactly what modules you need to use but the more practice here the better. You need to at least make use of a modal.

(10/10) You need to setup some sort of register and login system, do some simple research to find examples.

(5/5 points) There should be a minimum of 5 commits on your project, be sure to commit often!

(5/5 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.

(10/10 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations. You will need to explain the steps of initializing the database and then how to run the development server for your project.
Remember to run these commands and have them in your README:

python manage.py makemigrations (this will create any SQL entries that need to go into the database)

python manage.py migrate (this will apply the migrations)

python manage.py createsuperuser (this will create the administrator login for your /admin side of your project)
