int redled = 3;
void setup(){
    pinMode(redled, OUTPUT);
}
void loop(){
    for(int i = 0;i <256;i++){
        analogWrite(redled,i);
        delay(50);
    }
    
    for(int i = 255;i >= 0;i--){
        analogWrite(redled,i);
        delay(50);
    }
}