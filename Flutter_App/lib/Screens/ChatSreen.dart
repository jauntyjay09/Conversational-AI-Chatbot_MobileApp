import 'dart:convert';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:async';

import 'package:unibot_app/constants.dart';

class contact extends StatefulWidget {
    static final String ID='/chat';

  @override
  _contactState createState() => _contactState();
}

class ChatMessage{
  String messageContent;
  String messageType;
  ChatMessage({required this.messageContent, required this.messageType});
}

class _contactState extends State<contact> {
  final fieldText = TextEditingController();
  String msg='',dmes="";
  int start=0;

  List<ChatMessage> messages = [];


  void getData(String incoming_message) async {
    http.Response response = await http.get(
      Uri.parse("https://vbot-lgdolbmwka-uc.a.run.app/MainAlgo/ClientMessage=$incoming_message"),);
    try {
      setState(() {
        print(response.statusCode);
        if (response.statusCode == 200) {
          var decodedData = jsonDecode(response.body);
          print(decodedData);
          print(decodedData==null);
          // print(decodedData['name']);
          if(decodedData!=null)
          {
            var message=decodedData['message'];
            // names=name.toString();
            // ages=age.toString();
            // cabins=cabin.toString();
            // mobiles=mobile.toString();
            msg=message;
            print(msg);
            setState(() {
              messages.add(ChatMessage(messageContent:msg,messageType: "receiver"));
            });
          }

        } else {
          print(response.statusCode);
          setState(() {
            messages.add(ChatMessage(messageContent:"Sorry  details not available",messageType: "receiver"));
          });
        }
      });
    } catch (e) {
      print(e);
      setState(() {
        messages.add(ChatMessage(messageContent:"Sorry I dont understand,Try again later",messageType: "receiver"));
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        elevation: 0,
        automaticallyImplyLeading: false,
        backgroundColor: kpurpleColor,
        flexibleSpace: SafeArea(
          child: Container(
            padding: EdgeInsets.only(right: 16),
            child: Row(
              children: <Widget>[
                IconButton(
                  onPressed: (){
                    Navigator.pop(context);
                  },
                  icon: Icon(Icons.arrow_back,color: kSubColour,),
                ),
                SizedBox(width: 2,),
                // SizedBox(width: 12,),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: <Widget>[
                      Text("Buddy",style: TextStyle( fontSize: 16 ,fontWeight: FontWeight.w600,color:Colors.white),),
                      SizedBox(height: 6,),
                      Text("Online",style: TextStyle(color: Colors.grey.shade200, fontSize: 13),),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
      body: SizedBox(
        child: Container(
          color: kBackgroundColor,
          child: Stack(
            children: <Widget>[
              SingleChildScrollView(
                padding:EdgeInsets.only(bottom:50),
                child: ListView.builder(
                  itemCount: messages.length,
                  shrinkWrap: true,
                  padding: EdgeInsets.only(top: 10,bottom: 10),
                  physics: NeverScrollableScrollPhysics(),
                  itemBuilder: (context, index){
                    return  Container(

                      padding: EdgeInsets.only(left: 14,right: 14,top: 10,bottom: 10),
                      child: Align(
                        alignment: (messages[index].messageType == "receiver"?Alignment.topLeft:Alignment.topRight),
                        child: Container(
                          margin:(messages[index].messageType  == "receiver"?EdgeInsets.only(right:80.0):EdgeInsets.only(left: 50.0)),
                          decoration: BoxDecoration(
                            borderRadius: BorderRadius.circular(20),
                            color: (messages[index].messageType  == "receiver"?kCardColor:kpurpleColor),
                          ),
                          padding: EdgeInsets.all(16),
                          child: Text(messages[index].messageContent, style: TextStyle(fontSize: 15,color:Colors.white),),
                        ),
                      ),
                    );
                  },
                ),
              ),
              Align(
                alignment: Alignment.bottomLeft,
                child: Container(
                  padding: EdgeInsets.only(left: 10,bottom: 10,top: 10),
                  height: 50,
                  width: double.infinity,
                  color: kCardColor,
                  child: Row(
                    children: <Widget>[
                      SizedBox(width: 15,),
                      Expanded(
                        child: TextField(
                          controller: fieldText,
                          onChanged: (value){
                            dmes=value;
                          },
                          decoration: InputDecoration(
                              hintText: "Message...",
                              hintStyle: TextStyle(color: Colors.white),
                              border: InputBorder.none
                          ),
                        ),
                      ),
                      SizedBox(width: 15,),
                      FloatingActionButton(
                        onPressed: (){
                          messages.add(ChatMessage(messageContent: dmes,messageType: "sender"));
                         getData(dmes);
                          fieldText.clear();
                        },
                        child: Icon(Icons.send,color: Colors.white,size: 18,),
                        backgroundColor: Color(0xff13212e),
                        elevation: 0,
                      ),
                    ],

                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}