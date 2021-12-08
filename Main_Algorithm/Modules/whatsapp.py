
from flask_restful import Resource , reqparse ,abort ,fields,marshal_with
from fireo.models import Model
from fireo.fields import ListField,IDField,TextField

general_resource_fields={
    'message':fields.String
}
#--------------------Whatsapp--------#
#args
#whatsapp args
whatsapp_args=reqparse.RequestParser()
whatsapp_args.add_argument("description",type=str)
whatsapp_args.add_argument("tokens",action='append')


#marshal resource

whatsapp_resource_fields ={
    'id':fields.String,
    'description':fields.String
}

#Models
class whatsappmodel(Model):
    id=IDField()
    description=TextField()
    tokens=ListField()

#Whatsapp model    
Whatsapp_key ='whatsappmodel/'
class Whatsapp(Resource):
    @marshal_with(general_resource_fields)
    def put(self,whatsapp_id):
        args=whatsapp_args.parse_args()
        result = whatsappmodel.collection.get(Whatsapp_key+whatsapp_id)
        if(result is None):
            whatsappmodel.collection.create(id=str(whatsapp_id),description=args['description'],tokens=args['tokens'])
            return {"message":"success inserted the data"},201
        else :
            abort(409,message="Key is reserved/taken")

    @marshal_with(whatsapp_resource_fields)
    def get(self,whatsapp_id):
        result = whatsappmodel.collection.get(Whatsapp_key+whatsapp_id)
        if(result is None):
            abort(404,message="Key is invalid")
        else :
            return result.to_dict()
    
    @marshal_with(general_resource_fields)
    def patch(self,whatsapp_id):
        args=whatsapp_args.parse_args()
        u= whatsappmodel.collection.get(Whatsapp_key+whatsapp_id)
        if(u is None):
            abort(404,message="Key doesn't exist")
            
        if args['description']:
            u.description=args['description']
        if args['tokens']:
            u.tokens=args['tokens']
        u.update()
        return {"message":"updated the data"}    

    @marshal_with(general_resource_fields)
    def delete(self,whatsapp_id):
        result = whatsappmodel.collection.get(Whatsapp_key+whatsapp_id)
        if(result is None):
            abort(404,message="Key doesn't exist")
        else :
            whatsappmodel.collection.delete(Whatsapp_key+whatsapp_id)
            return {"message":"deleted the data"}

#sub doc
class programsmodel(Model):
    id=IDField()
    description=TextField()
    tokens=ListField()

#sub model    
class program(Resource):
    @marshal_with(general_resource_fields)
    def put(self,whatsapp_id,program_id):
        Parent_Program_key='whatsappmodel/'+whatsapp_id
        Programs_key ='whatsappmodel/'+whatsapp_id+'/programsmodel/'
        args=whatsapp_args.parse_args()
        result = programsmodel.collection.get(Programs_key+program_id)
        if(result is None):
            programsmodel.collection.create(parent=Parent_Program_key,id=str(program_id),description=args['description'],tokens=args['tokens'])
            return {"message":"success inserted the data"},201
        else :
            abort(409,message="Key is reserved/taken")

    @marshal_with(whatsapp_resource_fields)
    def get(self,whatsapp_id,program_id):
        Programs_key ='whatsappmodel/'+whatsapp_id+'/programsmodel/'
        result = programsmodel.collection.get(Programs_key+program_id)
        if(result is None):
            abort(404,message="Key is invalid")
        else :
            return result.to_dict()
    
    @marshal_with(general_resource_fields)
    def patch(self,whatsapp_id,program_id):
        Programs_key ='whatsappmodel/'+whatsapp_id+'/programsmodel/'
        args=whatsapp_args.parse_args()
        u= programsmodel.collection.get(Programs_key+program_id)
        if(u is None):
            abort(404,message="Key doesn't exist")
            
        if args['description']:
            u.description=args['description']
        if args['tokens']:
            u.tokens=args['tokens']
        u.update()
        return {"message":"updated the data"}    

    @marshal_with(general_resource_fields)
    def delete(self,whatsapp_id,program_id):
        Programs_key ='whatsappmodel/'+whatsapp_id+'/programsmodel/'
        result = programsmodel.collection.get(Programs_key+program_id)
        if(result is None):
            abort(404,message="Key doesn't exist")
        else :
            programsmodel.collection.delete(Programs_key+program_id)
            return {"message":"deleted the data"}


#sub-sub doc
class branchmodel(Model):
    id=IDField()
    description=TextField()
    tokens=ListField()

#sub-sub model
class branch(Resource):
    @marshal_with(general_resource_fields)
    def put(self,whatsapp_id,program_id,branch_id):
        Parent_Program_key='whatsappmodel/'+whatsapp_id+'/programsmodel/'+program_id
        Programs_key ='whatsappmodel/'+whatsapp_id+'/programsmodel/'+program_id+'/branchmodel/'
        args=whatsapp_args.parse_args()
        result = branchmodel.collection.get(Programs_key+branch_id)
        if(result is None):
            branchmodel.collection.create(parent=Parent_Program_key,id=str(branch_id),description=args['description'],tokens=args['tokens'])
            return {"message":"success inserted the data"},201
        else :
            abort(409,message="Key is reserved/taken")

    @marshal_with(whatsapp_resource_fields)
    def get(self,whatsapp_id,program_id,branch_id):
        Programs_key ='whatsappmodel/'+whatsapp_id+'/programsmodel/'+program_id+'/branchmodel/'
        result = branchmodel.collection.get(Programs_key+branch_id)
        if(result is None):
            abort(404,message="Key is invalid")
        else :
            return result.to_dict()
    
    @marshal_with(general_resource_fields)
    def patch(self,whatsapp_id,program_id,branch_id):
        Programs_key ='whatsappmodel/'+whatsapp_id+'/programsmodel/'+program_id+'/branchmodel/'
        args=whatsapp_args.parse_args()
        u= branchmodel.collection.get(Programs_key+branch_id)
        if(u is None):
            abort(404,message="Key doesn't exist")
            
        if args['description']:
            u.description=args['description']
        if args['tokens']:
            u.tokens=args['tokens']
        u.update()
        return {"message":"updated the data"}    

    @marshal_with(general_resource_fields)
    def delete(self,whatsapp_id,program_id,branch_id):
        Programs_key ='whatsappmodel/'+whatsapp_id+'/programsmodel/'+program_id+'/branchmodel/'
        result = branchmodel.collection.get(Programs_key+branch_id)
        if(result is None):
            abort(404,message="Key doesn't exist")
        else :
            branchmodel.collection.delete(Programs_key+branch_id)
            return {"message":"deleted the data"}

#endpoint creation

#------------END Whatsapp-------------#