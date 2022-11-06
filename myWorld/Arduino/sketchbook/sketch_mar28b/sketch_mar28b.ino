int sensor = A0;
void setup(){
    Serial.begin(9600);
}

void loop(){
    float a = analogRead(sensor);
    Serial.print("The water level is ");
    Serial.println(a);
    delay(1000);
}