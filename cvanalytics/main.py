import graphene

from graphene_mongo import MongoengineObjectType
from flask import Flask
from flask_graphql import GraphQLView
from models import User as UserModel
from models import Intents as IntentModel
from models import Network as NetworkModel
from mongoengine import connect
from flask_cors import CORS
from flask import request
import pandas as pd

app = Flask(__name__)

CORS(app)

#app.debug = True
#connect("twittercovid", host='localhost:27017')

connect("twittercovid", host='mongodb+srv://username:pwd@cluster0.ezrhe.mongodb.net/?ssl=true&ssl_cert_reqs=CERT_NONE',alias="default")
class User(MongoengineObjectType):
    class Meta:
        model = UserModel

class Intents(MongoengineObjectType):
    class Meta:
        model = IntentModel

class Network(MongoengineObjectType):
    class Meta:
        model = NetworkModel

class Query(graphene.ObjectType):
    users = graphene.List(User)
    intents = graphene.List(Intents)
    networks = graphene.List(Network)

    def resolve_users(self, info):
        return list(UserModel.objects.all())

    def resolve_intents(self, info):
        return list(IntentModel.objects.all())

    def resolve_networks(self, info):
        return list(NetworkModel.objects.all())

schema = graphene.Schema(query=Query)


query = '''
    query {
        networks {
            text
        }
    }
'''
result = schema.execute(query)
print(result)

app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)




if __name__ == "__main__":
    #app.run(host = "0.0.0.0",port = 5001)
    app.run()