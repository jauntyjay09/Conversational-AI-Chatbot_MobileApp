import 'package:flutter/material.dart';
import 'package:unibot_app/constants.dart';

class AuthButtons extends StatelessWidget {
  AuthButtons({required this.text,required this.ontap});
  final String text;
  final Function()? ontap;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: ontap,
      child: Card(
        color: kredcolour,
        shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(20.0)
        ),
        margin: EdgeInsets.symmetric(vertical: 10.0,horizontal: 20.0),
        child: ListTile(
          title:Center(
            child: Text(
                text
            ),
          ),
        ),
      ),
    );
  }
}
