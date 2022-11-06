int redLed = 11;

void setup(){
    pinMode(redLed, OUTPUT);
}
void loop(){
    
  for(int i=0; i <= 255; i++){
        i = i+4;
        analogWrite(redLed,i);
        delay(1000);
        
    }
}