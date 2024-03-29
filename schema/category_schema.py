from flask import Flask, jsonify
from marshmallow import Schema, fields


class CategorySchema(Schema):
    message = fields.String()
    data = fields.Raw()
