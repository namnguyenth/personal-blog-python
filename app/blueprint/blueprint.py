import os

from flask import Blueprint
from flask_restx import Api

from route import blog

blueprint = Blueprint("api", __name__)
api = Api(
    blueprint,
    title="Campus people",
    version="1.0",
    description="Campus people service",
    prefix=os.environ.get("API_PREFIX", "/api"),
)

api.add_namespace(blog, path="/blog")