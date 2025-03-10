// this is a program to blink 3 leds
// variable called red_led  assign 12 
int red_led  = 11;
int blue_led = 10;
int green_led = 9;
//set up function 

void setup() {
  // this is part of code that runs once
    pinMode(red_led, OUTPUT);  // pin 12 to act as an output
    pinMode(blue_led, OUTPUT);  // pin 12 to act as an output
    pinMode(green_led, OUTPUT);  // pin 12 to act as an output
}

void loop(){
    // part of code that runs continously /repeatedly
    digitalWrite(red_led, HIGH); // turn on led in pin 12
    digitalWrite(blue_led, LOW); // turn on led in pin 11
    digitalWrite(green_led, HIGH); // turn on led in pin 12

    delay(500);   // wait for 500 milliseconds = half a sec
    digitalWrite(red_led, LOW); // turn off led in pin 12
    digitalWrite(blue_led, HIGH); // turn off led in pin 12
    digitalWrite(green_led, LOW); // turn off led in pin 12
    delay(500);  // wait for 500 milliseconds = half a sec
}