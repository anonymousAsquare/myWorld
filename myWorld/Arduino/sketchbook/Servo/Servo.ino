#include <Servo.h>
int servoPin = 9;
int servoDeg1 = 160;
int servoDeg2 = 0;
int led = 3;
int led1 = 5;
int led2 = 6;
int led3 = 7;
Servo data;

void setup() {
    Serial.begin(9600);
    pinMode(led, OUTPUT);
    pinMode(led1, OUTPUT);
    pinMode(led2, OUTPUT);
    pinMode(led3, OUTPUT);
    data.attach(servoPin);
  
}

void loop() {
   
    for(int i = 0 ; i <= 250; i++){
        analogWrite(led, i);
        analogWrite(led1, i);
        analogWrite(led2, i);
        analogWrite(led3, i);
            data.write(servoDeg1);
            delay(100);

        
        
    }
    
    for(int i = 250; i >= 0; i--){
        analogWrite(led, i);
        analogWrite(led1, i);
        analogWrite(led2, i);
        analogWrite(led3, i);
            data.write(servoDeg2);
        delay(100);
        }  
        
}

