from datetime import datetime
from extensions import db
from sqlalchemy import UUID, text as sa_text

class User(db.Model):
    __tablename__ = 'user'
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, server_default=sa_text("uuid_generate_v4()"))
    user_name = db.Column(db.String(250), unique=True)
    password = db.Column(db.String(50))
    created_date = db.Column(db.DateTime,default=datetime.now(), nullable=True)
    created_by = db.Column(UUID(as_uuid=True))
    deleted_date = db.Column(db.DateTime, nullable=True)
    deleted_by = db.Column(UUID(as_uuid=True))


class MtCategory(db.Model):
    __tablename__ = 'mt_category'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    blog = db.relationship("Blog")


class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    slug = db.Column(db.String(250))
    category_id = db.Column(db.Integer, db.ForeignKey("mt_category.id"))