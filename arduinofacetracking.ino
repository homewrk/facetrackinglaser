#include <Servo.h>
int x;
int y;

Servo servoX;
Servo servoY;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(1);
  servoX.attach(5);
  servoY.attach(6); 
}

void loop() {
  while (!Serial.available()):
    x = Serial.readString().toInt();
    y = Serial.readString().toInt();
  
  servoX.write(x);
  servoY.write(y);

}
