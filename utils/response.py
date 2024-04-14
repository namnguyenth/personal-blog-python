from marshmallow import Schema, fields, pre_dump


class Responses:
    @staticmethod
    def normal_response(data):
        return {"data": data, "message": "success", "success": True}

    @staticmethod
    def normal_response_without_data():
        return {"message": "success", "success": True}

    @staticmethod
    def deleted_response():
        return {"message": "deleted", "success": True}

    @staticmethod
    def bad_request_response(message):
        return {"data": None, "message": message, "success": False}

    @staticmethod
    def not_found_request_response(message):
        return {"data": None, "message": message, "success": False}

    @staticmethod
    def server_error_request_response(message):
        return {"data": None, "message": message, "success": False}


class BaseResponseSchema(Schema):
    success = fields.Boolean(default=True)
    message = fields.String()

    @pre_dump
    def preprocess(self, in_data, **kwargs):
        out_data = {
            "success": in_data["success"],
            "data": in_data["data"],
            "message": in_data["message"],
        }
        return out_data

