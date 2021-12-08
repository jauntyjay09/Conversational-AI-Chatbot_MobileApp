from flask_restful import Resource , reqparse ,abort ,fields,marshal_with
from fireo.models import Model
from fireo.fields import IDField,TextField


general_resource_fields={
    'message':fields.String
}

#-------------hostel complaint student module--------#


#args
#complaint-hostel
hostel_complaint_args=reqparse.RequestParser()
hostel_complaint_args.add_argument("hostel-name",type=str)
hostel_complaint_args.add_argument("room-no",type=str)
hostel_complaint_args.add_argument("student-name",type=str)
hostel_complaint_args.add_argument("student-registrationId",type=str)
hostel_complaint_args.add_argument("date",type=str)
hostel_complaint_args.add_argument("complaint",type=str)

#marshal resource
hostel_complaint_resource_fields ={
    'Date':fields.String,
    'RegId':fields.String,
    'StudentName':fields.String,
    'RoomNo':fields.String,
    'Complaint':fields.String
}
#Models
#hostel category model
class hostelcatmodel(Model):
    id=IDField()
    description=TextField()
    
hostelcat_key ='hostelcatmodel/'
class hostelcat(Resource):
    @marshal_with(general_resource_fields)
    def put(self,hostelname_id):
        args=hostel_complaint_args.parse_args()
        result = hostelcatmodel.collection.get(hostelcat_key+hostelname_id)
        if(result is None):
            hostelcatmodel.collection.create(id=str(hostelname_id),description=args['hostel-name'])
            return {"message":"success inserted the data"},201
        else :
            abort(409,message="Key is reserved/taken")

#sub doc individual hostels
class hostelcomplaintmodel(Model):
    id = IDField()
    HostelName = TextField()
    RoomNo = TextField()
    StudentName = TextField()
    RegId = TextField()
    Date = TextField()
    Complaint = TextField()

#class/doc
class hostelcomplaint(Resource):
    @marshal_with(general_resource_fields)
    def put(self,hostelname_id,complaint_id):
        Parent_hostelcomplaint_key='hostelcatmodel/'+hostelname_id
        complaint_key ='hostelcatmodel/'+hostelname_id+'/hostelcomplaintmodel/'
        args=hostel_complaint_args.parse_args()
        result = hostelcomplaintmodel.collection.get(complaint_key+complaint_id)
        if(result is None):
            hostelcomplaintmodel.collection.create(
                parent=Parent_hostelcomplaint_key,id=str(complaint_id),
                HostelName=args['hostel-name'],
                RoomNo=args['room-no'],
                StudentName=args['student-name'],
                RegId=args['student-registrationId'],
                Date=args['date'],
                Complaint=args['complaint']
                )
            return {"message":"success inserted the data"},201
        else :
            abort(409,message="Key is reserved/taken")

    # @marshal_with(hostel_complaint_resource_fields)
    def get(self,hostelname_id,complaint_id):
        complaint_key ='hostelcatmodel/'+hostelname_id+'/hostelcomplaintmodel/'
        result = hostelcomplaintmodel.collection.get(complaint_key+complaint_id)
        complaints = hostelcomplaintmodel.collection.parent('hostelcatmodel/'+hostelname_id).fetch() 
        data=[]
        for c in complaints:
            item = {'id':c.id,'hostel-name':c.HostelName,'RoomNo':c.RoomNo,'Student-Name':c.StudentName,'RegId':c.RegId,'Date':c.Date,'Complaint':c.Complaint}
            data.append(item)
        return data
        # if(result is None):
        #     abort(404,message="Key is invalid")
        # else :
        #     return result.to_dict()


# class hosteladmin(Resource):


#endpoint creation

#=============end hostel complaint student module======#

