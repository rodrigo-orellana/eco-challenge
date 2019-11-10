from flask import Flask
from flask_restful import Resource, Api
import datetime

app = Flask(__name__)
api = Api(app)


class Hello(Resource):
    def get(self, name):
        return {"Hello": name}


var = Hello()
print (var.get("pelao"))
print (datetime.date(2019, 11, 4))
