from flask_restful import Resource, reqparse
from models.stores import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        else:
            {'message': 'Store not found'}, 404


    def post(self, name):
        store = StoreModel.find_by_name(name)
        if store is None:
            new_store = StoreModel(name)
            try:
                new_store.save_to_db()
            except:
                return {'message': 'New store could not be created'},500
        else:
            return {'message': 'Store with the name {} already exits'.format(name)}, 400

    def delete(self, name):
            store = StoreModel.find_by_name(name)
            if store:
                StoreModel.delete_from_db(store)
            return {'message':  'Store deleted'}


class StoresList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
