This is a simple skeleton for building Flask applications using my preferred structure and toolchain:

[Flask](http://flask.pocoo.org/)

[MongoDB](http://www.mongodb.org/)

[Heroku](https://www.heroku.com/)

[Bootstrap](http://twitter.github.io/bootstrap/)

[jQuery](http://jquery.com/)

Use it as a jumping off point for quickly prototyping applications.


WHAT'S IN THE BOX
=================

Backend
-------

	Flask

	Flask-MongoEngine

	Flask-Login

	Flask-Assets (jsmin/cssmin)

	gunicorn


Frontend
--------

	jQuery 2.0.2

	Bootstrap 2.3.2

	Modernizer 2.6.2


Amenities
---------

Basic user auth is provided

	/register
	/login
	/logout



Prerequisites
=============

[pip](http://guide.python-distribute.org/installation.html)

[virtualenv](http://guide.python-distribute.org/virtualenv.html)

[foreman](https://toolbelt.heroku.com/)



Installation and Usage
======================


Start off by cloning the project

	$ git clone git@github.com:david-torres/flask-quickstart.git myapp

remove the git directory, you'll be initializing your own

	$ cd myapp
	$ rm -rf .git

build the virtual environment

    $ virtualenv --distribute venv
    $ source venv/bin/activate

install packages

    $ pip install -r requirements.txt

run the app

    $ foreman app.py

edit the config and add your own values in

	$ nano application/config.py

init your own git repo

	$ git init
	$ git add .
	$ git commit -m "init"

deploy to heroku

	$ heroku create
	$ git push heroku master

set the environment variable on heroku to use production config

	$ heroku config:set APP_ENV='production'


