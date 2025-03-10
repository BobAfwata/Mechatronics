
/*
  This is a program to blink an led when the button is pressed
  Date : 10/3/2025
  Bob Afwata
*/

int red_led    = 11; //red led connected to pin 11
int red_button = 2; // red button connected to pin 2
//set up function 

void setup() {
  // this is part of code that runs once
    pinMode(red_led, OUTPUT);  // pin 12 to act as an output
    pinMode(red_button, INPUT);  // pin 12 to act as an output
    
}

void loop(){
  int is_pressed = 0;
  is_pressed  = digitalRead(red_button);
  if(is_pressed == LOW){

    digitalWrite(red_led , HIGH);
  }else{
      digitalWrite(red_led , LOW);
  }
    
}