import re
import requests
from flask import Flask, views,render_template
from flask_restful import Api,Resource , reqparse ,abort ,fields,marshal_with
from fireo.models import Model, model
from fireo.fields import ListField,BooleanField,IDField,NumberField,TextField,NestedModel

general_resource_fields={
    'message':fields.String
}
#------------Hostel------------------#

#args
#hostel args
hostel_args=reqparse.RequestParser()
hostel_args.add_argument("floor",type=str)
hostel_args.add_argument("timings",type=str)
hostel_args.add_argument("tokens",action='append')

#marshal resource
hostel_resource_fields ={
    'description':fields.String 
}

#Models
class Hostelmodel(Model):
    id = IDField()
    timings = TextField()
    floor = TextField()
    tokens=ListField()

#class/doc
#hostel model    
Hostel_key='hostelmodel/'
class Hostel(Resource):
    @marshal_with(general_resource_fields)
    def put(self,hostel_id):
        args=hostel_args.parse_args()
        result = Hostelmodel.collection.get(Hostel_key+hostel_id)
        if(result is None):
            Hostelmodel.collection.create(id=str(hostel_id),tokens=args['tokens'],floor=args['floor'],timings=args['timings'])
            return {"message":"success inserted the data"},201
        else :
            abort(409,message="Key is reserved/taken")

    @marshal_with(hostel_resource_fields)
    def get(self,hostel_id):
        result = Hostelmodel.collection.get(Hostel_key+hostel_id)
        if(result is None):
            abort(404,message="Key is invalid")
        else :
            description=f'Below are the details of {result.id} :\n Floor :\n It is in {result.floor} floor\n Timings are :\n {result.timings} '
            return {'description':description}
    
    @marshal_with(general_resource_fields)
    def patch(self,hostel_id):
        args=hostel_args.parse_args()
        u = Hostelmodel.collection.get(Hostel_key+hostel_id)
        if(u is None):
            abort(404,message="Key doesn't exist")     
        if args['floor']:
            u.floor=args['floor']
        if args['timings']:
            u.timings=args['timings']
        if args['tokens']:
            u.tokens=args['tokens']
        u.update()
        return {"message":"updated the data"}    

    @marshal_with(general_resource_fields)
    def delete(self,hostel_id):
        result = Hostelmodel.collection.get(Hostel_key+hostel_id)
        if(result is None):
            abort(404,message="Key doesn't exist")
        else :
            Hostelmodel.collection.delete(Hostel_key+hostel_id)
            return {"message":"deleted the data"}

#endpoint creation

#--------------END Hostel------------#
