# :snake: Python Code Along

After completing the [Codecademy Course](https://www.codecademy.com/learn/python) for Python, I wanted to get some hands on experience using a Python framework so I followed a great tutorial on [scotch.io](https://scotch.io/). This application uses Python 2.7.X.


This is a simple Web App that uses the [Flask](http://flask.pocoo.org/) microframework and connects to a MySQL database and performs simple CRUD actions via [MySQL-Python](https://pypi.python.org/pypi/MySQL-python/1.2.5) and the [Flask-sqlalchemy ORM](http://flask-sqlalchemy.pocoo.org/2.1/). Database migrations use [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/). It also performs user authentication using [Flask-Login](https://flask-login.readthedocs.io/en/latest/) and secures forms with [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/).


As of right now, the application is at the end of Part 1 of the code along. But it was deployed in that state, so it features sign up and login pages as well as an authenicated dashboard page.


What was not covered in the Tutorial was deploying the webpage to Heroku (but it does cover deploying to a different service). I have documented a Heroku deployment here. Assuming you have the Heroku CLI set up, then this should document the whole process.



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


In order to perform the Database migrations, you will need to use MySQL to `CREATE DATABASE dreamteam_db;` and then call the migratrion from the command line using `$ flask db upgrade`.



## Deployment to Heroku

This assumes that you have the Heorku CLI set up and have deployed to the service in the past, maybe in a different programming language. More in depth info on basics can be found in this [Tutorial](http://kennmyers.github.io/tutorial/2016/03/11/getting-flask-on-heroku.html) for Python's Flask Deployment.


Once your projected is Initilized in Heroku, go to your Heroku dashboard and click on the Heroku Add Ons. In this case, we want the Free JawsDB Add On to support the MySQL features of the app. Once JawsDB is added, click on JawsDB icon in Heroku to navigate to their page. The JawsDB page will show you your connection information. Add the database connection string to the production case in the `instance/config.py` file. The production case is under the `else` statement.


You can also use the database connection information from JawsDB to create a `New Connection` in MySQL WorkBench (if you have that installed. Since we use the SQLAlchemy ORM, though, we can force our migration (without MySQL WorkBench) using the hacky approach below. First, we set the local envirnoment variable to production, which will cause our database to connect to the JawsDB database instead of the local database. Then we run the migration, knowing we are connected to the JawsDB account. Finally, we set the local evironment variable back to development to prevent messing up the deployed database in the future. 

  ```
    export FLASK_CONFIG=production
    flask db upgrade
    export FLASK_CONFIG=development

  ```


With the JawsDB, database set up, we can finally deploy the app for real. Using a buildpack finally got the app working for me, so I suggest that you use it as well. Below, are the BSAH commands that I used to successfully deploy to Heroku.

  ```
     $ heroku config:add BUILDPACK_URL=https://github.com/kennethreitz/conda-buildpack.git
     $ heroku config:set FLASK_CONFIG=production
     $ git push heroku master
  ```


And that should do it! Your app **should be** deployed, complete with working Log In and Register features thanks to JawsDB. If you have issues, be sure to `git add .`, `git commit -m "your edits"`, and `git push origin master` before trying to deploy again via `git push heroku master`.



## Resources

[Set Up Virtual Env and Flask](https://scotch.io/tutorials/getting-started-with-flask-a-python-microframework)

[CRUD Web App with Flask - Part 1](https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one)

[CRUD Web App with Flask - Part 2](https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-two)

[CRUD Web App with Flask - Part 3](https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-three)



## Screenshots

#### Home Page
![HomePage](/screenshots/HomePage.png)

#### Login Page
![Log In Page](/screenshots/LoginPage.png)

#### Registration Page
![Register Page](/screenshots/RegisterPage.png)