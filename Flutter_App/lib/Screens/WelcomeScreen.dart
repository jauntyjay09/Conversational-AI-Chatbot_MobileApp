import 'package:animated_text_kit/animated_text_kit.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:unibot_app/Screens/HostelComplaintsScreen.dart';
import 'package:unibot_app/Screens/LoginScreen.dart';
import 'package:unibot_app/Screens/RegistrationScreen.dart';
import 'package:unibot_app/components/AuthButtons.dart';
import 'package:unibot_app/constants.dart';
import 'package:unibot_app/components/UserInputBox.dart';

class WelcomeScreen extends StatefulWidget {
  static final String ID ='/';
  @override
  _WelcomeScreenState createState() => _WelcomeScreenState();
}

class _WelcomeScreenState extends State<WelcomeScreen> {
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
                height: 60.0,
              ),
            ),
            Text('UniBud',
              style: TextStyle(
                  fontFamily: 'Pacifico',
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
            AuthButtons(
                text: 'Login',
                ontap:  (){
                  Navigator.pushNamed(context, LoginScreen.ID);
                }
            ),
            SizedBox(
              height: 20.0,
              width: 135.0,

            ),
            AuthButtons(
                text: 'Register',
                ontap:  (){
                  Navigator.pushNamed(context, RegistrationScreen.ID);
                }
            )
          ],
        ),
      ),
    );
  }
}

