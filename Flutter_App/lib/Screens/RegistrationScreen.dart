import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:unibot_app/Screens/LoginScreen.dart';
import 'package:unibot_app/constants.dart';
import 'package:unibot_app/components/AuthButtons.dart';
import 'package:unibot_app/components/UserInputBox.dart';
class RegistrationScreen extends StatefulWidget {
  static final String ID ='/register';
  @override
  _RegistrationScreenState createState() => _RegistrationScreenState();
}

class _RegistrationScreenState extends State<RegistrationScreen> {

  String name="",email="",password="";
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
                name=value;
              },
                obscuretext: false,
                hintext: 'Name',
                icon: FontAwesomeIcons.userTie,
                keyboard: TextInputType.name),
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
            AuthButtons(text: 'Register',
            ontap: (){
               // print(name+" "+email+" "+password);
              Navigator.pushNamed(context, LoginScreen.ID);
            },
            ),

          ],
        ),
      ),
    );
  }
}
