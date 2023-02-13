import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env   


# create an instance of the imported Flask() class, and store it in a
# variable called 'app', which takes the default Flask __name__ module

app = Flask(__name__)

# then specify two app configuration variables, which come from our
# environment variables

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# then create an instance of the imported SQLAlchemy() class, which will
# be assigned to a variable 'db', and set to the instance of our Flask
# app on l11

db = SQLAlchemy(app)

# finally, from our taskmanager package, we will import a file called 'routes'

from taskmanager import routes
