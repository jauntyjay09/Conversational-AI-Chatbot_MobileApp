from flask_restful import Resource ,fields,marshal_with


from Modules import contacts , whatsapp ,hostel

general_resource_fields={
    'message':fields.String
}
# -----------NLP--------------------#

nlp_resource_fields={
    'Code':fields.Integer,
    'Message':fields.String,
    'Intent':fields.String
}


def get_intent(key_list,income_message):
    flag=False
    Parent_key=''
    intent=''
    for doc_key in key_list:
        for token in doc_key.tokens:
            token=token.lower()
            if token in income_message:
                intent=doc_key.id
                Parent_key=doc_key.key
                flag=True
                break
        if(flag):
            break
    return intent,Parent_key

def whatsappIntent(input_message):
    main_intent=''
    parent_key=''
    main_key_list = whatsapp.whatsappmodel.collection.fetch()
    Mintent,MPKey=get_intent(main_key_list,input_message)   
    if Mintent :
        main_intent='/'+Mintent
        parent_key=MPKey
        first_sub_key_list=whatsapp.programsmodel.collection.parent(MPKey).fetch()
        fintent,fPKey=get_intent(first_sub_key_list,input_message)
        if fintent:
            main_intent+='/'+fintent
            parent_key=fPKey
            second_sub_key_list=whatsapp.branchmodel.collection.parent(fPKey).fetch()
            sintent,sPKey=get_intent(second_sub_key_list,input_message)
            if sintent:
                main_intent+='/'+sintent
                parent_key=sPKey

        # print('intent is '+main_intent+" parent key is "+parent_key)
    return main_intent

def hostelIntent(input_message):
    main_intent=''
    parent_key=''
    main_key_list=hostel.Hostelmodel.collection.fetch()
    Mintent,MPKey=get_intent(main_key_list,input_message)
    return Mintent

def contactIntent(input_message):
    main_key_list=contacts.contactmodel.collection.fetch()
    Mintent,MPKey=get_intent(main_key_list,input_message)
    return Mintent   

class NLP(Resource):
    @marshal_with(nlp_resource_fields)
    def get(self,input_message):
        Cintent=contactIntent(input_message)
        if Cintent :
            return {"Code":200,"Message":"Intent found","Intent":'contact/'+Cintent}
        Hintent=hostelIntent(input_message)
        if Hintent :
            return {"Code":200,"Message":"Intent found","Intent":'hostel/'+Hintent}
        Wintent=whatsappIntent(input_message)
        if Wintent :
            return {"Code":200,"Message":"Intent found","Intent":'whatsapp'+Wintent}
            
        return {"Code":404,"Message":"Not found any Intents"}


#---------------END NLP -------------#