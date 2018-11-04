# This is a file
from app import db
from app import login
# from flask_login import UserMixin
# @login.user_loader
# def load_user(id):
#     return Classroom.query.get(int(id))

# class User(UserMixin, db.Model):
class Classroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    instructor = db.Column(db.String(140), index=True)
    active = db.Column(db.Boolean, index=True)
    # password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<Classroom {}>'.format(self.id)

class Student(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('classroom.id'))
    name = db.Column(db.String(140), primary_key=True)


    def __repr__(self):
        return '<Student {}>'.format(self.name)
