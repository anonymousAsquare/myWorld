int led1 = 11; //Green led
int led2 = 10; //Yellow led
int led3 = 13; //Red led
int button = 2; 
int buzzer = 6;
//boolean buttonValue = false;
void setup(){
    pinMode(led1, OUTPUT);
    pinMode(led2, OUTPUT);
    pinMode(led3, OUTPUT);
    pinMode(button, INPUT);
    pinMode(buzzer, OUTPUT);
   
    
}
void loop(){
   int buttonR = digitalRead(button);
    if(buttonR == 1){
    //buttonValue = !buttonValue;2
     // delay(100);
    digitalWrite(led2, HIGH);
    delay(70);
    digitalWrite(led3, HIGH);
    delay(70);
    digitalWrite(led1, HIGH);
    delay(70);
    tone(buzzer, 900, 300);
    delay(200);
    tone(buzzer, 800, 200);
    delay(100);
   
  
    
    digitalWrite(led1, LOW);
    delay(70);
    digitalWrite(led2, LOW);
    delay(70);
    digitalWrite(led3, LOW);
    delay(70);
       }
    else{
        digitalWrite(led1, LOW);
        digitalWrite(led2, LOW);
        digitalWrite(led3, LOW);
    }
}