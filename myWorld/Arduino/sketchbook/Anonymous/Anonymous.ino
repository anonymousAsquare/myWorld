int trigPin = 9; 
int echoPin = 10;
int buzzer = 11; 
int ledPin = 13; // defines variables 

float duration;
float distance; 
float speedOfSound = 343; 

void setup() {
    Serial.begin(9600);
     pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
     pinMode(echoPin, INPUT); // Sets the echoPin as an Input
     pinMode(buzzer, OUTPUT);
     pinMode(ledPin, OUTPUT);
     
     } 
    void loop() { 
      // Clears the trigPin 
        digitalWrite(trigPin, LOW);
         delayMicroseconds(2000); // Sets the trigPin on HIGH state for 2000 micro seconds 
        digitalWrite(trigPin, HIGH);
         delayMicroseconds(15);
         digitalWrite(trigPin, LOW); // Reads the echoPin, returns the sound wave travel time in microseconds */
        duration = pulseIn(echoPin, HIGH);
     // Calculating the distance
         duration = duration / 1000000.;
    distance = speedOfSound * duration;
    distance = distance / 2;
    distance = distance * 1000;
    
    // Prints the distance on the Serial Monitor
         Serial.print("Distance: ");
         Serial.print(distance);
         Serial.println(" mm");
         delay(1000);
    
         if (distance <= 100){ 
              digitalWrite(buzzer, HIGH); 
              digitalWrite(ledPin, HIGH); 
            } 
        else{  
             digitalWrite(buzzer, LOW);   
            digitalWrite(ledPin, LOW); }
      }