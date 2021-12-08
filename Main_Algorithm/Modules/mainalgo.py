import requests 
from flask_restful import Resource ,fields,marshal_with

general_resource_fields={
    'message':fields.String
}

url="https://vbot-lgdolbmwka-uc.a.run.app/"
#------------MainRun--------#
class MainAlgo(Resource):
    @marshal_with(general_resource_fields)
    def get(self,incoming_msg):
        incoming_msg =incoming_msg.lower()
        responded = False
        if 'hi' in incoming_msg:
            botmessage = 'Hey, Welcome to VIT-AP Services \nhow can I help you?'
            response=botmessage
            responded = True   
        NLPUrl=url+"NLP/ClientMessage="+incoming_msg
        NLPresponse=requests.get(NLPUrl)
        if  NLPresponse.status_code == 200:
            data=NLPresponse.json()
            if data["Code"] == 200 :
                Intent=data["Intent"]
                finalUrl=url+Intent
                finalresponse=requests.get(finalUrl)
                if finalresponse.status_code==200:
                    Hdata = finalresponse.json()
                    botmessage =Hdata['description']
                else:
                    botmessage='Service Unavailable'
                response=botmessage
                responded=True
        if not responded:
            response='I am learning and growing day by day\nDeveloped by- Jayakumar MHK  :)'
        return {'message':response}
 


#------------END MainRun-----#
