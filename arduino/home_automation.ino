#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include "DHT.h"


#define SCREEN_WIDTH 128  // 128 pixels width
#define SCREEN_HEIGHT 64  

int sensor_pin = 26;  
float light_intensity = 0.0; // decimal point 27.8

int red_button = 2;
int blue_button = 6;
int green_button = 3;

int red_led = 11;
int green_led = 2;

int counter = 0;
bool buttonPressed = false;  // Track button state

// Initialize OLED display
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

//dht
#define DHTPIN     7    
#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321

DHT dht(DHTPIN, DHTTYPE);


//stepper motor 
byte directionPin = 21;
byte stepPin = 20;
int numberOfSteps = 200;
int pulseWidthMicros = 20;  // microsecondo
int millisbetweenSteps = 150; // milliseconds - or try 100 for slower steps
int statostart;

void run_motor(); // function prototype

void setup() {
  dht.begin();

  //light sensor pin
  pinMode(sensor_pin, INPUT);
  //leds as output 
  pinMode(red_led, OUTPUT);
  pinMode(green_led, OUTPUT);

   // buttons as input pullup
  pinMode(red_button, INPUT_PULLUP);
  pinMode(blue_button, INPUT_PULLUP);
  pinMode(green_button, INPUT_PULLUP);

  // stepper motor pins
  pinMode(directionPin, OUTPUT);
  pinMode(stepPin, OUTPUT);

  Serial.begin(115200);

  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("SSD1306 allocation failed"));
    for (;;);
  }

  delay(2000);
  display.clearDisplay();
  display.setTextSize(1);  // Adjust text size 1,2 3
  display.setTextColor(WHITE);
}

void loop() {
  // Read light intensity
  light_intensity = analogRead(sensor_pin);

  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();


  // Check if any reads failed and exit early (to try again).
  if (isnan(temperature) || isnan(humidity)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }

  Serial.print(F("Humidity: "));
  Serial.print(humidity);
  Serial.print(F("%  Temperature: "));
  Serial.print(temperature);
  Serial.println(F("°C "));

  // Print to Serial Monitor
  Serial.print("Light Intensity: ");
  Serial.println(light_intensity);
 // chack if light intensity is above 500 lux
  if(light_intensity > 500){
    digitalWrite(red_led, HIGH);
    digitalWrite(green_led, LOW);
    run_motor();
  }
  else{
    digitalWrite(red_led, LOW);
    digitalWrite(green_led, HIGH);
  }

  // Check if button is pressed (with debouncing)
  if (digitalRead(red_button) == LOW) { 
    if (!buttonPressed) {  // Only increment once per press
      counter++;  
      buttonPressed = true;
    }
  } else {
    buttonPressed = false;  // Reset when released
  }

  // Check if button is pressed (with debouncing)
  if (digitalRead(blue_button) == LOW) { 
    if (!buttonPressed) {  // Only increment once per press
      counter--;  
      buttonPressed = true;
    }
  } else {
    buttonPressed = false;  // Reset when released
  }

  // control motor 
 //  if(digitalRead(green_button) == LOW){
 //      run_motor();
 //  }


  // Display values on OLED
  display.clearDisplay();
  display.setCursor(0, 10);
  display.print("LUX: ");
  display.println(light_intensity);
  
  display.setCursor(0, 30);
  display.print("Temp: ");
  display.println(temperature);
  
  display.display();

  delay(100);
}

void run_motor()
{
      digitalWrite(directionPin, HIGH);
      digitalWrite(stepPin, HIGH);
      delayMicroseconds(pulseWidthMicros); 
      digitalWrite(stepPin, LOW);
      /*
      for(int n = 0; n < numberOfSteps; n++) {
      digitalWrite(stepPin, HIGH);
      delayMicroseconds(pulseWidthMicros); 
      digitalWrite(stepPin, LOW);
      delay(millisbetweenSteps);

       }
     */ 
   
}