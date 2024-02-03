# Task-11
## TinkerCAD

This task is new to me. I haven't used the arduino before. It's interesting. I write a code in C++ program to function the arduino for an automatic retractable roof in a farming environment.

<Checkout:> https://www.tinkercad.com/things/bN58BcqpbIS-amfoss-task-11/editel?returnTo=%2Fdashboard

## Materials used:
- Arduino UNO board
- Breadboard Small
- Photoresistor
- Resistor ohm
- Micro Servo
- LCD 16x2

## Code

```
#include <Servo.h>
#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
Servo myServo;

const int sensorPin = A0;
int sensorValue = 0;
int angle;

void setup() {
  lcd.begin(16, 2);
  myServo.attach(9);
  Serial.begin(9600);

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Hello!");
  delay(2000);
  lcd.clear();
    lcd.print("...");
  delay(500);
  lcd.clear();
}

void loop() {
  sensorValue = analogRead(sensorPin);
  angle = map(sensorValue, 0, 1023, 0, 179);
  myServo.write(angle);
  delay(15);

  if (sensorValue > 300) {
    lcd.setCursor(0, 1);
    lcd.print("ROOF OPEN");
    delay(1000);
  } else {
    lcd.setCursor(0, 1);
    lcd.print("ROOF CLOSED");
    delay(1000);
  }
}

```





