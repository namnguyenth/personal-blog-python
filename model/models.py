from extensions import db


class Category(db.model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    blog = db.relationship("blog", back_populates="category")


class Blog(db.model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    slug = db.Column(db.String(250))
    category = db.Column(db.ForeignKey("category.id"), primary_key=True)