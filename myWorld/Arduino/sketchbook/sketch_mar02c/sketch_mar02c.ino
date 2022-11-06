int micPin = A0;
int led = 13;
boolean isOn = false;
int micValue;
int micValue1;

void setup(){
    Serial.begin(9600);
    pinMode(micPin, INPUT);
    pinMode(led,OUTPUT);
    
}

void loop(){
    micValue = analogRead(micPin);
    Serial.println(micValue);
    delay(5);
    
    micValue1 = analogRead(micPin);
    Serial.println(micValue);
    
   
    if(micValue - micValue1 > 2|| micValue1 - micValue >2){
        isOn = !isOn;
        delay(5);
            digitalWrite(led, isOn);
    }
}