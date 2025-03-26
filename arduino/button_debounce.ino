#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128  
#define SCREEN_HEIGHT 64  

int sensor_pin = 26;  
float light_intensity = 0.0;
int button_pin = 2;
int counter = 0;
bool buttonPressed = false;  // Track button state

// Initialize OLED display
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

void setup() {
  pinMode(sensor_pin, INPUT);
  pinMode(button_pin, INPUT_PULLUP);
  Serial.begin(115200);

  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("SSD1306 allocation failed"));
    for (;;);
  }

  delay(2000);
  display.clearDisplay();
  display.setTextSize(1);  // Adjust text size
  display.setTextColor(WHITE);
}

void loop() {
  // Read light intensity
  light_intensity = analogRead(sensor_pin);

  // Print to Serial Monitor
  Serial.print("Light Intensity: ");
  Serial.println(light_intensity);

  // Check if button is pressed (with debouncing)
  if (digitalRead(button_pin) == LOW) { 
    if (!buttonPressed) {  // Only increment once per press
      counter++;  
      buttonPressed = true;
    }
  } else {
    buttonPressed = false;  // Reset when released
  }

  // Display values on OLED
  display.clearDisplay();
  display.setCursor(0, 10);
  display.print("LUX: ");
  display.println(light_intensity);
  
  display.setCursor(0, 30);
  display.print("Counter: ");
  display.println(counter);
  
  display.display();

  delay(100);
}
