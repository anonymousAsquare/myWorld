int led = 8;
int buzzer = 9;
int trigPin = 10;
int echoPin = 11;
float speedOfSound = 323;
float duration;
float distance;

void setup(){
    pinMode(led, OUTPUT);
    pinMode(buzzer, OUTPUT);
    pinMode(echoPin, INPUT);
    pinMode(trigPin, OUTPUT);
}

void loop(){
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2000);
    
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(15);
    
    digitalWrite(trigPin, LOW);
    
    duration = pulseIn(echoPin, HIGH);
    duration = duration / 1000000;
    distance = duration * speedOfSound;
    distance = distance/2.;
    distance = distance * 1000;
    
    if(distance < 100){
        digitalWrite(led, HIGH);
        digitalWrite(buzzer, HIGH);
 
    }
    else{
        digitalWrite(led,LOW);
        digitalWrite(buzzer,LOW);
    }
    }