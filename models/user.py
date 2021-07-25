import sqlite3
from db import db


class UserModel(db.Model):

    __tablename__ = 'usertable'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40))
    password = db.Column(db.String(40))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
        # connection = sqlite3.connect("mydb.db")
        # cursor = connection.cursor()
        #
        # query = "select * from usertable where username = ?"
        # result = cursor.execute(query, (username,)) #paraameters should be in tuple
        #
        # row = result.fetchone()
        #
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None
        #
        # connection.close()
        # return user

    @classmethod
    def find_by_userid(cls, _id):
        return cls.query.filter_by(id=_id).first()
        # connection = sqlite3.connect("mydb.db")
        # cursor = connection.cursor()
        #
        # query = "select * from usertable where id = ?"
        # result = cursor.execute(query, (_id,))  # paraameters should be in tuple
        #
        # row = result.fetchone()
        #
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None
        #
        # connection.close()
        # return user