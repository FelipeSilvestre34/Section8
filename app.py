from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from Db import db, security

from security import authenticate, identity
from Resources.user import UserRegister
from Resources.item import Item, ItemList
from Resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Section6.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = security
api = Api(app)

#cria todas as tabelas necessárias para que o app rode
@app.before_first_request
def create_table():
    db.create_all()

jwt = JWT(app, authenticate, identity)


#http://127.0.0.1:5000/
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
