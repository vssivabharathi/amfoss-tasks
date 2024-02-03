# Task-11
## TinkerCAD

This task is new to me. I haven't used the arduino before. It's interesting. I write a code in C++ program to function the arduino for an automatic retractable roof in a farming environment.

<Checkout:> https://www.tinkercad.com/things/bN58BcqpbIS-amfoss-task-11/editel?returnTo=%2Fthings%2FbN58BcqpbIS-amfoss-task-11

## Materials used:
- Arduino UNO board
- Breadboard Small
- Photoresistor
- Resistor 10k ohm
- Micro Servo

## Code

```
#include <Servo.h>
Servo myServo;

const int sensorPin = A0;
int sensorValue = 0;
int angle;

void setup() {
  myServo.attach(9);
  Serial.begin (9600);
  
}

void loop() {
  sensorValue = analogRead (sensorPin);
  angle = map(sensorValue, 0, 1023, 0, 179);
  myServo.write(angle);
  delay (15);

}

```





