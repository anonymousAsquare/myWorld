#include <LiquidCrystal.h>
LiquidCrystal lcd(10, 9, 5, 4, 3, 2);
int trigPin = 8;
int echoPin = 1;
int red = 13;
int green = 12;
int blue = 11;
int buzzer = 7;
float distance;
float duration;
int speedOfLight = 323;

void setup(){
    lcd.begin(16,2);
    lcd.setCursor(0,0);
    lcd.print("Distance: ");
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
    pinMode(red, OUTPUT);
    pinMode(blue, OUTPUT);
    pinMode(green, OUTPUT);
    pinMode(buzzer, OUTPUT);
    
}

void loop(){
    digitalWrite(trigPin, LOW);
    delayMicroseconds(1000);
    
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(15);
    
    digitalWrite(trigPin, LOW);
    
    duration = pulseIn(echoPin, HIGH);
    
    duration = duration/1000000;
    
    distance = duration * speedOfLight;
    
    distance = distance/2.;
    
    distance = distance * 100;
    
    lcd.setCursor(0,1);
    lcd.print(distance);
    lcd.print(" cm");
    delay(1000);
    
    if(distance <= 5){
       digitalWrite(red, HIGH);
       digitalWrite(green, LOW);
       digitalWrite(blue, LOW);
       tone(buzzer, 800, 400);
        
    }
    else if(distance > 5 && distance < 180){
        digitalWrite(blue, HIGH);
        digitalWrite(green, LOW);
        digitalWrite(red, LOW);
        //analogWrite(blue, 250);
        delay(1000);
    }
    else if(distance > 180){
        digitalWrite(green, HIGH);
        digitalWrite(red, LOW);
        digitalWrite(blue, LOW);
        //analogWrite(green, 250);
        delay(1000);
    }
}