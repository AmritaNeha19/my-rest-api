import sqlite3
from db import db


class ItemModel(db.Model):

    __tablename__ = 'itemstable'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('storestable.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price,store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

        # connection = sqlite3.connect("mydb.db")
        # cursor = connection.cursor()
        # get_item_query = "select * from itemstable where name = ?"
        # result = cursor.execute(get_item_query, (name,))
        # row = result.fetchone()
        #
        # if row:
        #     #return {'name': row[0], 'price': row[1]}, 200
        #     return cls(*row)  # same as return cls(row[0], row[1])  #return object

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

        # connection = sqlite3.connect('mydb.db')
        # cursor = connection.cursor()
        #
        # query = "insert into itemstable values(?,?)"
        # cursor.execute(query, (self.name, self.price))
        # connection.commit()
        # connection.close()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

        # connection = sqlite3.connect('mydb.db')
        # cursor = connection.cursor()
        #
        # query = "update itemstable set price=? WHERE name=?"
        # cursor.execute(query, (self.price, self.name))
        # connection.commit()
        # connection.close()

