from flask import Flask, jsonify, abort, make_response, request
from flask.ext.restful import Api, Resource, reqparse, fields, marshal_with
from server.dao import ManufacturerDAO
import json
from server import app, api

resource_fields = {
'pkey': fields.Integer,
'name': fields.String
}

print(__name__)

class ManufacturerAPI(Resource):
    @marshal_with(resource_fields)
    def get(self):
        manufacturers = ManufacturerDAO.getManufacturers()
        return manufacturers

class TestAPI(Resource):
    def get(self):
        return "HELLO"#{"TESTING": "TESTING"}





api.add_resource(ManufacturerAPI, '/api/v1.0/manufacturer', endpoint='manufacturer')
api.add_resource(TestAPI, '/test', endpoint='/test')
