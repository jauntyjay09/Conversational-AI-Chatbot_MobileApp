import 'package:flutter/material.dart';
import '../constants.dart';


class UserInputBox extends StatelessWidget {
  UserInputBox({required this.onchanged, required this.obscuretext ,required this.hintext,required this.icon,required this.keyboard});

  final String hintext;
  final IconData icon;
  final Function(String)? onchanged;
  final TextInputType keyboard;
  final bool obscuretext;

  @override
  Widget build(BuildContext context) {
    return Card(
      color: kCardColor,
      shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(20.0)
      ),
      margin: EdgeInsets.symmetric(vertical: 10.0,horizontal: 20.0),
      child: ListTile(
        leading:Icon(
          icon,
          color: kMainColour,
        ),
        title:TextField(
          onChanged: onchanged,
          decoration: InputDecoration(
            border: InputBorder.none,
            hintStyle: kSubtext,
            hintText: hintext,
          ),
          keyboardType: keyboard,
          style: kMaintext,
          obscureText: obscuretext,
          cursorColor: kMainColour,
        ),
      ),
    );
  }
}
