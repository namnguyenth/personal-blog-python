from flask import Flask, jsonify
from marshmallow import Schema, fields


class UserSchema(Schema):
    message = fields.String()
    data = fields.Raw()
    