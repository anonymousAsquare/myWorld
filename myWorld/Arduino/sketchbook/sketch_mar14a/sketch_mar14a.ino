#include <LiquidCrystal.h>
LiquidCrystal lcd(10, 9, 5, 4, 3, 2);
int i = 0;

void setup(){
    lcd.begin(16, 2);
    lcd.setCursor(0, 0);
    lcd.print("AnonymousAsquare");
}

void loop(){
    for (i = 1; i <= 10; i++){
        lcd.setCursor(0, 1);
        lcd.print(i);
        lcd.print(" Second(s)");
        delay(1000);
    }
    
    for (i = 10; i >= 1; i--){
        lcd.setCursor(0, 1);
        lcd.print(i);
        lcd.print(" Second(s)");
        delay(1000);
    }

}