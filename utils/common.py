import uuid

from model.models import User


class Common():
    def uuid_generator():
        while True:
            new_uuid = uuid.uuid4()
            query = User.query.filter_by(uuid=new_uuid)
            account = query.first()

            if not account:
                new_uuid
                break

        return new_uuid

