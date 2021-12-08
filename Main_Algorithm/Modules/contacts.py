from flask_restful import Resource , reqparse ,abort ,fields,marshal_with
from fireo.models import Model
from fireo.fields import ListField,IDField,TextField


general_resource_fields={
    'message':fields.String
}
#---------------Whom to Contact-------#


#args
Contact_args=reqparse.RequestParser()
Contact_args.add_argument("email",type=str)
Contact_args.add_argument("name",type=str)
Contact_args.add_argument("info",type=str)
Contact_args.add_argument("tokens",action='append')
#marshal resource
contact_resource_fields={
    'description':fields.String
}
#Models
class contactmodel(Model):
    id=IDField()
    email=TextField()
    name=TextField()
    info=TextField()
    tokens=ListField()

#class/doc
Contact_key='contactmodel/'
class contact(Resource):
    @marshal_with(general_resource_fields)
    def put(self,contact_id):
        args=Contact_args.parse_args()
        result = contactmodel.collection.get(Contact_key+contact_id)
        if(result is None):
            contactmodel.collection.create(id=str(contact_id),tokens=args['tokens'],email=args['email'],name=args['name'],info=args['info'])
            return {"message":"success inserted the data"},201
        else :
            abort(409,message="Key is reserved/taken")

    @marshal_with(contact_resource_fields)
    def get(self,contact_id):
        result = contactmodel.collection.get(Contact_key+contact_id)
        if(result is None):
            abort(404,message="Key is invalid")
        else :
            description=f' Below are the details for {result.id} :\n Name : {result.name} \nEmail :\n  {result.email} \n Info :\n {result.info} '
            return {'description':description}
    
    @marshal_with(general_resource_fields)
    def patch(self,contact_id):
        args=Contact_args.parse_args()
        u = contactmodel.collection.get(Contact_key+contact_id)
        if(u is None):
            abort(404,message="Key doesn't exist")     
        if args['email']:
            u.email=args['email']
        if args['name']:
            u.name=args['name']
        if args['info']:
            u.info=args['info']
        if args['tokens']:
            u.tokens=args['tokens']
        u.update()
        return {"message":"updated the data"}    

    @marshal_with(general_resource_fields)
    def delete(self,contact_id):
        result = contactmodel.collection.get(Contact_key+contact_id)
        if(result is None):
            abort(404,message="Key doesn't exist")
        else :
            contactmodel.collection.delete(Contact_key+contact_id)
            return {"message":"deleted the data"}


#endpoint creation

#---------------END whom to contact---#