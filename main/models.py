from FlaskProj import db


class User(db.Document):
    name = db.StringField()
    password = db.StringField()


class Services(db.Document):
    name = db.StringField()
    description = db.StringField()


class Products(db.Document):
    name = db.StringField()
    description = db.StringField()
    price = db.IntField();
