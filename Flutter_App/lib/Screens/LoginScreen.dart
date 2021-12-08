import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:unibot_app/Screens/ChatSreen.dart';
import 'package:unibot_app/Screens/MainScreen.dart';
import 'package:unibot_app/Screens/WelcomeScreen.dart';
import 'package:unibot_app/components/AuthButtons.dart';
import 'package:unibot_app/components/UserInputBox.dart';
import 'package:unibot_app/constants.dart';

class LoginScreen extends StatefulWidget {
  static final String ID ='/login';
  @override
  _LoginScreenState createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  String email="",password="";
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      resizeToAvoidBottomInset: false,
      body: SafeArea(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Hero(
              tag: 'logo',
              child: Container(
                child: Image.asset('images/buddylogo.png'),
                height: 100.0,
              ),
            ),
            Text('UniBud',
              style: TextStyle(
                  fontFamily: 'Pacifico',
// letterSpacing: 0,
                  fontSize: 30.0,
                  color: kredcolour,
                  fontWeight: FontWeight.bold
              ),

            ),
            SizedBox(
              height: 20.0,
              width: 135.0,
              child: Divider(
                color: Colors.blue.shade200,
              ),
            ),
            UserInputBox(
              onchanged: (value){
                email=value;
              },
              icon: FontAwesomeIcons.at,
              hintext: 'Email',
              obscuretext: false,
              keyboard: TextInputType.emailAddress,
            ),
            UserInputBox(
              onchanged: (value){
                password=value;
              },
              icon: FontAwesomeIcons.key,
              hintext: 'Password',
              obscuretext: true,
              keyboard: TextInputType.text,
            ),
            AuthButtons(text: 'Login',
            ontap: (){
              if(email=="jayakumar.18bce7031@vitap.ac.in" &&  password == "Jauntyjay09"){
                Navigator.pushNamed(context, MainScreen.ID);
              }
              else{
                return showDialog(
                  context: context,
                  builder: (ctx) => AlertDialog(
                    title: Text("Invalid Credits!!!"),
                    content: Text("You have Entered Invalid Credentials Kindly Check"),
                    actions: <Widget>[
                      FlatButton(
                        onPressed: () {
                          Navigator.of(ctx).pop();
                        },
                        child: Text("OK"),
                      ),
                    ],
                  ),
                );
              }

            },
            ),
            Text(
              'Forgot Password ?',
              style: kSubtext,
            ),
          ],
        ),
      ),
    );
  }
}


