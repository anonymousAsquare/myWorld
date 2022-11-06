int led = 13;
int buzzer = 11;
int flamesensor = A0;

void setup(){
    
    Serial.begin(9600);
    pinMode(led, OUTPUT);
    pinMode(buzzer, OUTPUT);
    pinMode(flamesensor, INPUT);
   
}

void loop(){
    
    int sensor = analogRead(flamesensor);
    
    //Serial.print("The flame reading is ");
  //  Serial.println(flamesensor);
    
    if(sensor < 1023){
        
        
        digitalWrite(led, HIGH);
        delay(200);
        tone(buzzer, 800, 800);
        digitalWrite(led, LOW);
        delay(200);
        tone(buzzer, 1000, 800);
        //delay(200);
        
    }
    
    else{
        
       digitalWrite(led, LOW);
       digitalWrite(buzzer, LOW);
       delay(200);
    }
    

   
}