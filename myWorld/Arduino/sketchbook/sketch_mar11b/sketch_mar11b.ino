int led = 3;
int led1 = 5;
int led2 = 6;
int led3 = 7;

void setup(){
    pinMode(led, OUTPUT);
    pinMode(led1, OUTPUT);
    pinMode(led2, OUTPUT);
    pinMode(led3, OUTPUT);
    
}
void loop(){
    digitalWrite(led1, HIGH);
    digitalWrite(led, HIGH);
    delay(2000);
    
    digitalWrite(led1, LOW);
    digitalWrite(led, LOW);
    delay(500);
    
    digitalWrite(led2, HIGH);
    digitalWrite(led, HIGH);
    delay(2000);
    
    digitalWrite(led2, LOW);
    digitalWrite(led, LOW);
    delay(500);
    
    digitalWrite(led3, HIGH);
    digitalWrite(led, HIGH);
    delay(2000);
    
    digitalWrite(led3, LOW);
    digitalWrite(led, LOW);
    delay(500);
   
    
}