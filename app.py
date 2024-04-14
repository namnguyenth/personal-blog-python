import os
from flask import Flask
from flask.cli import load_dotenv
# from dotenv import load_dotenv

from extensions import api, db
from resources import ns
from route import (
    blog,
    category,
    auth
)
# load_dotenv()


def create_app():
    # DB_URL = "postgresql://{user}:{pw}@{url}/{db}".format(
    #     user=os.environ.get("POSTGRES_USER"),
    #     pw=os.environ.get("POSTGRES_PW"),
    #     url=os.environ.get("POSTGRES_URL"),
    #     db=os.environ.get("POSTGRES_DB"),
    # )

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://personal:12345678@personal.cf4kuad7cfau.ap-southeast-1.rds.amazonaws.com:5432/postgres"

    api.init_app(app)
    db.init_app(app)

    api.add_namespace(blog.blog_api)
    api.add_namespace(ns)
    api.add_namespace(category.category_api)
    api.add_namespace(auth.auth_api)

    return app
