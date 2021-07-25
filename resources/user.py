import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="Username cannot be blank")
    parser.add_argument('password', type=str, required=True, help="Password cannot be blank")

    def post(self):

        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "User already exits"}, 400

        user = UserModel(data['username'], data['password'])
        user.save_to_db()

        # connection = sqlite3.connect('mydb.db')
        # cursor = connection.cursor()
        # insert_user = "insert into usertable values (NULL ,? ,?)"
        # cursor.execute(insert_user, (data['username'], data['password'],))
        #
        # connection.commit()
        # connection.close()
        return {"message": "User created"}, 201

