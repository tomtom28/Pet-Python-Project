# Python Code Along

After completing the [Codecademy Course](https://www.codecademy.com/learn/python) for Python, I wanted to get some hands on experience using a Python framework so I followed a great tutorial on [scotch.io](https://scotch.io/). This application uses Python 2.7.


This is a simple Web App that uses the [Flask](http://flask.pocoo.org/) microframework and connects to a MySQL database and performs simple CRUD actions via [MySQL-Python](https://pypi.python.org/pypi/MySQL-python/1.2.5) and the [Flask-sqlalchemy ORM](http://flask-sqlalchemy.pocoo.org/2.1/). Database migrations use [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/). It also performes user authentication using [Flask-Login](https://flask-login.readthedocs.io/en/latest/) and secures forms with [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/).


As of right now, the application is at the end of Part 1 of the code along.


What was not covered in the Tutorial was delpoying the webpage to Heroku (but it does cover deploying to a different service). I have documented a Heroku deployment here. Assuming you have the Heroku CLI set up, then this show document the whole process.


## Running Locally

In the project folder, install all the requirements dependencies.

  ```
    $ pip install -r requirements.txt
  ```


Inside the `instance` folder, rename the `config.test.py` file to `config.py`. 
Then, add the proper connection information for your MYSQL database.


Assuming you have virtualenv virtualenvwrapper, initiliaze a virtual envirnoment.

  ```
    $ export WORKON_HOME=~/Envs
    $ source /usr/local/bin/virtualenvwrapper.sh
    $ mkvirtualenv my-venv
    $ workon my-venv
  ```


In the project folder, configure the environment variables.
Note that Windows user may need to use `set` instead of `export`.

  ```
    $ export FLASK_CONFIG=development
    $ export FLASK_APP=run.py
    $ flask run
  ```


## Deployment to Heroku

This assumes that you have the Heorku CLI set up and have deployed to the service in the past, maybe in a different programming language.





## Resources

[Set Up Virtual Env and Flask](https://scotch.io/tutorials/getting-started-with-flask-a-python-microframework)

[CRUD Web App with Flask - Part 1](https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one)

[CRUD Web App with Flask - Part 2](https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-two)

[CRUD Web App with Flask - Part 3](https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-three)