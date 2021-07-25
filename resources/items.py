from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from models.items import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='Mandatory field')
    parser.add_argument('store_id', type=float, required=True, help='Mandatory field')

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return {"message": "Item {} exists".format(name)}, 400
        data = Item.parser.parse_args()
        #item = {'name': name, 'price': data['price']}
        item = ItemModel(name, data['price'], data['store_id'])

        try:
            #ItemModel.insert(item)
            #item.insert()
            item.save_to_db()
        except:
            return {'message': 'Error while inserting'}, 500

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'item deleted'}

        # item = ItemModel.find_by_name(name)
        # if item is None:
        #     return {'message': 'item does not exist'}
        # else:
        #     connection = sqlite3.connect('mydb.db')
        #     cursor = connection.cursor()
        #     query = "delete from itemstable where name = ?"
        #
        #     cursor.execute(query, (name,))
        #     connection.commit()
        #     connection.close()
        #     return {'message': 'item deleted'}

    def put(self, name):
        item = ItemModel.find_by_name(name)
        data = Item.parser.parse_args()

        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price']

        item.save_to_db()
        return item.json()

        # #updated_item = {'name': name, 'price': data['price']}
        # updated_item = ItemModel(name, data['price'])
        #
        # if item is None:
        #     try:
        #         #ItemModel.insert(updated_item)
        #         updated_item.insert()
        #     except:
        #         return {'message': 'Error inserting'}, 500
        # else:
        #     try:
        #         updated_item.update()
        #         #item.update()
        #     except:
        #         return {'message': 'Error updating'}, 500
        #
        # return updated_item.json()


class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
        #return {"items": list(map(lambda x: x.json(), ItemModel.query.all()))}
            # connection = sqlite3.connect('mydb.db')
            # cursor = connection.cursor()
            # query = "select * from itemstable"
            #
            # result = cursor.execute(query)
            # item_list = []
            #
            # for row in result:
            #     item_list.append({'name': row[1], 'price': row[2]})
            #
            # connection.commit()
            # connection.close()
            # return {'item': item_list}

