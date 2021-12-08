import 'package:flutter/material.dart';
import 'package:unibot_app/Screens/ChatSreen.dart';
import 'package:unibot_app/Screens/HostelComplaintsScreen.dart';
import 'package:unibot_app/Screens/LoginScreen.dart';
import 'package:flutter/services.dart';
import 'package:unibot_app/Screens/MainScreen.dart';
import 'package:unibot_app/Screens/RegistrationScreen.dart';
import 'package:unibot_app/Screens/WelcomeScreen.dart';
import 'package:unibot_app/constants.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  SystemChrome.setPreferredOrientations(
      [DeviceOrientation.portraitUp, DeviceOrientation.portraitDown]
  );
  runApp( UniBot());
}

class UniBot extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData.dark().copyWith(
          scaffoldBackgroundColor: kBackgroundColor
      ),
      initialRoute: WelcomeScreen.ID,
      routes: {
        LoginScreen.ID : (context) => LoginScreen(),
        WelcomeScreen.ID: (context) => WelcomeScreen(),
        RegistrationScreen.ID : (context) => RegistrationScreen(),
        MainScreen.ID : (context) => MainScreen(),
        HostelComplaintScreen.ID: (context) => HostelComplaintScreen(),
        contact.ID : (context) => contact(),
      },
    );
  }
}


