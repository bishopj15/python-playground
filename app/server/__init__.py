from flask import Flask
from flask.ext.restful import Api

app=Flask(__name__, static_url_path = "/", static_path = "/static")
api = Api(app)

import rest.ManufacturerAPI
