import 'package:flutter/material.dart';
import 'package:unibot_app/Screens/ChatSreen.dart';
import 'package:unibot_app/Screens/LoginScreen.dart';
import 'package:unibot_app/constants.dart';
import 'package:unibot_app/components/UserInputBox.dart';
import 'package:unibot_app/components/AuthButtons.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';


class MainScreen extends StatefulWidget {
  static final String ID ='/mainscreen';
  @override
  _MainScreenState createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      resizeToAvoidBottomInset: false,
      appBar: AppBar(
        elevation: 0,
        automaticallyImplyLeading: false,
        backgroundColor: kBackgroundColor,
        flexibleSpace: SafeArea(
          child: Container(
            padding: EdgeInsets.only(right: 16),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.end,
              children: <Widget>[
                SizedBox(width: 10.0),
                Hero(
                  tag: 'logo',
                  child: Container(
                    child: Image.asset('images/buddylogo.png'),
                    height:50.0,
                  ),
                ),
                SizedBox(width: 10.0),
                Expanded(
                  child:Text('UniBud',
                    style: TextStyle(
                        fontFamily: 'Pacifico',
// letterSpacing: 0,
                        fontSize: 25.0,
                        color: kredcolour,
                        fontWeight: FontWeight.bold
                    ),

                  ),
                ),
              ],
            ),
          ),
        ),
      ),
      body:SafeArea(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            GestureDetector(
              onTap: (){
                Navigator.pushNamed(context,contact.ID);
              },
              child: Card(
                color: kCardColor,
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(20.0)
                ),

                margin: EdgeInsets.symmetric(vertical: 10.0,horizontal: 20.0),

                child: Column(
                  children: [
                    SizedBox(height: 20.0),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Hero(
                          tag: 'bot',
                          child: Container(
                            child: Image.asset('images/chatbot.png'),
                            height: 60.0,
                          ),
                        ),
                        Text('Chat',
                          textAlign: TextAlign.center,
                          style: TextStyle(
                              fontFamily: 'Pacifico',
// letterSpacing: 0,
                              fontSize: 30.0,
                              color: kMainColour,
                              fontWeight: FontWeight.bold
                          ),

                        ),
                      ],
                    ),
                    SizedBox(height: 20.0),
                  ],
                ),
              ),
            ),


          ],
        ),
      ) ,
    );

  }
}
