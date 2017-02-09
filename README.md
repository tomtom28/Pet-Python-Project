# Pet-Python-Project

After completing the [Codecademy Course](https://www.codecademy.com/learn/python) for Python, I wanted to get some hands on experience using a Python framework so I followed a great tutorial on [scotch.io](https://scotch.io/). This application uses Python 2.7.x.


This is a simple Web App that uses the [Flask](http://flask.pocoo.org/) microframework and connects to a MySQL database and performs simple CRUD actions via [MySQL-Python](https://pypi.python.org/pypi/MySQL-python/1.2.5) and the [Flask-sqlalchemy ORM](http://flask-sqlalchemy.pocoo.org/2.1/). Database migrations use [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/). It also performes user authentication using [Flask-Login](https://flask-login.readthedocs.io/en/latest/).


Notes to self....
Future idea is to webscrape from [http://abc13.com/tag/snake/](http://abc13.com/tag/snake/).


Need to continue at...
https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one#auth-blueprint


## Running Locally

In the project folder, install all the requirements dependencies.
  `$ pip install -r requirements.txt`


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



## Resources

[Set Up Virtual Env and Flask](https://scotch.io/tutorials/getting-started-with-flask-a-python-microframework)

[CRUD Web App with Flask - Part 1](https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one)

[CRUD Web App with Flask - Part 2](https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-two)

[CRUD Web App with Flask - Part 3](https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-three)