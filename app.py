import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from Resources.user import UserRegister
from Resources.item import Item, ItemList
from Resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///Section6.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'felipe'
api = Api(app)

#cria todas as tabelas necessárias para que o app rode

jwt = JWT(app, authenticate, identity)


#http://127.0.0.1:5000/
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    from Db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
