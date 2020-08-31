#include <Servo.h>
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;

void setup() {
  servo1.attach(8);
  servo2.attach(9);
  servo3.attach(10);
  servo4.attach(11);
  servo5.attach(12);
  /*pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(9, OUTPUT);*/
  Serial.begin(9600);
  delay(1000);
}

void loop() {
  if(Serial.available()){
    int input = Serial.read();
    Serial.print(input);
    input = input - 48;
    switch(input){
      case 0:
        //shut_down();
        //digitalWrite(13, HIGH);
        servo1.write(0);
        servo2.write(180);
        servo3.write(0);
        servo4.write(0);
        servo5.write(0);
        break;
      case 1:
        //shut_down();
        //digitalWrite(13, HIGH);
        servo1.write(0);
        servo2.write(180);
        servo3.write(0);
        servo4.write(0);
        servo5.write(180);
        break;
      case 2:
        //shut_down();
        //digitalWrite(13, HIGH);
        //digitalWrite(12, HIGH);
        servo1.write(180);
        servo2.write(180);
        servo3.write(0);
        servo4.write(0);
        servo5.write(180);
        break;
      case 3:
        /*shut_down();
        digitalWrite(13, HIGH);
        digitalWrite(12, HIGH);
        digitalWrite(11, HIGH);*/
        servo1.write(180);
        servo2.write(180);
        servo3.write(0);
        servo4.write(180);
        servo5.write(180);
        break;
      case 5:
        /*shut_down();
        digitalWrite(13, HIGH);
        digitalWrite(12, HIGH);
        digitalWrite(11, HIGH);
        digitalWrite(10, HIGH);*/
        servo1.write(180);
        servo2.write(0);
        servo3.write(180);
        servo4.write(180);
        servo5.write(180);
        break;
       case 4:
        /*shut_down();
        digitalWrite(13, HIGH);
        digitalWrite(12, HIGH);
        digitalWrite(11, HIGH);
        digitalWrite(10, HIGH);
        digitalWrite(9, HIGH);*/
        servo1.write(0);
        servo2.write(0);
        servo3.write(180);
        servo4.write(180);
        servo5.write(180);
        break;
    }
  }
}

/*void shut_down(){
  digitalWrite(13, LOW);
  digitalWrite(12, LOW);
  digitalWrite(11, LOW);
  digitalWrite(10, LOW);
  digitalWrite(9, LOW);
}*/
