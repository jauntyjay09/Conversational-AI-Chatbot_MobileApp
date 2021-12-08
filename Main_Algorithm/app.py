import re
import requests
from flask import Flask, views,render_template
from flask_restful import Api,Resource , reqparse ,abort ,fields,marshal_with
from fireo.models import Model, model
from fireo.fields import ListField,BooleanField,IDField,NumberField,TextField,NestedModel
from Modules import contacts , hostel ,hostelcomplaint , mainalgo , nlp ,whatsapp 

app = Flask(__name__)
api = Api(app)



#====================endpoints=========================#

#-----------------MainAlgo----------------#

api.add_resource(mainalgo.MainAlgo,"/MainAlgo/ClientMessage=<string:incoming_msg>")

#-----------------NLP---------------------#

api.add_resource(nlp.NLP,"/NLP/ClientMessage=<string:input_message>")

#----------------hostel-------------------#

api.add_resource(hostel.Hostel,"/hostel/<string:hostel_id>")

#----------------whatsapp-----------------#

api.add_resource(whatsapp.Whatsapp,"/whatsapp/<string:whatsapp_id>")
api.add_resource(whatsapp.program,"/whatsapp/<string:whatsapp_id>/<string:program_id>")
api.add_resource(whatsapp.branch,"/whatsapp/<string:whatsapp_id>/<string:program_id>/<string:branch_id>")


#-----------------hostel_complaint-------#

api.add_resource(hostelcomplaint.hostelcat,"/hostelcomplaints/<string:hostelname_id>")
api.add_resource(hostelcomplaint.hostelcomplaint,"/hostelcomplaints/<string:hostelname_id>/<string:complaint_id>")

#----------------contacts----------------#

api.add_resource(contacts.contact,"/contact/<string:contact_id>")



#==================Endpoints over========#



#------sample---#

#args

#marshal resource

#Models

#class/doc

#endpoint creation


#---end sample---#

@app.route('/')
def index():
    return render_template('index.html')



if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT',8080)))
