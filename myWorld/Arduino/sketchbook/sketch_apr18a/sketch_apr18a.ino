int led1 = 8;
int led2 = 9;
int led3 = 10;

void setup(){
    pinMode(led1,OUTPUT);
    pinMode(led2,OUTPUT);
    pinMode(led3,OUTPUT);
}
void loop(){
    for(int i =1; i<=15;i++){
        digitalWrite(led1, HIGH);
        delay(1000);
        digitalWrite(led1, LOW);
        delay(1000);
        }
    for(int i =1; i<=15;i++){
        digitalWrite(led2, HIGH);
        delay(1000);
        digitalWrite(led2, LOW);
        delay(1000);
    }
    for(int i =1; i<=15;i++){
        digitalWrite(led3, HIGH);
        delay(1000);
        digitalWrite(led3, LOW);
        delay(1000);
    }
}