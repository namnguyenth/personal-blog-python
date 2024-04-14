from flask import Flask, jsonify
from marshmallow import Schema, fields

from utils.response import BaseResponseSchema


class UserSchema(Schema):
    user_name = fields.String(required=False)
    password = fields.String(required=False)


class UserSchemaResponse(Schema):
    uuid = fields.String(required=True)
    user_name = fields.String(required=True)


class UserSchemaResponse1(BaseResponseSchema):
    data = fields.List(fields.Nested(UserSchemaResponse))


