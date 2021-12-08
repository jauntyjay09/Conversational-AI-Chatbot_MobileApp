import 'dart:convert';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:unibot_app/constants.dart';
import 'package:unibot_app/components/UserInputBox.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
class HostelComplaintScreen extends StatefulWidget {
  static final String ID = '/hostelcomplaints';
  @override
  _HostelComplaintScreenState createState() => _HostelComplaintScreenState();
}

class _HostelComplaintScreenState extends State<HostelComplaintScreen> {

  var  url =Uri.parse("https://vbot-lgdolbmwka-uc.a.run.app/hostelcomplaints/mh2/cv");
  List data=[];

  @override
  void initState() {
    super.initState();
    this.getJsonData();
  }

  Future<String> getJsonData() async {
    var response =await http.get(
      //encode url
       url,
      //only accept json response
      headers: {"Accept":"application/json"}
    );
    //print(response.body);

    setState(() {
      var convertDataToJson = jsonDecode(response.body);
      data = convertDataToJson;
    });
    return "Succcess";
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      resizeToAvoidBottomInset: false,
      body: SafeArea(
        child: ListView.builder(
          itemCount: data==null ? 0 :data.length,
          itemBuilder: (BuildContext context, int index) {
            return Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Card(
                  color: kCardColor,
                  shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(20.0)
                  ),
                  margin: EdgeInsets.symmetric(vertical: 10.0,horizontal: 20.0),
                  child: Column(
                    children: [
                      ListTile(
                        leading:Icon(
                          FontAwesomeIcons.at,
                          color: kMainColour,
                        ),
                        title:Text(
                            data[index]["RoomNo"],
                          style: kMaintext,
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            );
          },
        ),
      ),
    );
  }
}
