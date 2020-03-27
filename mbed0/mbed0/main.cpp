#include "mbed.h"


DigitalOut redLED(LED_RED);

DigitalOut greenLED(LED_GREEN);


int Led1(DigitalOut& ledpin);
int Led2(DigitalOut& ledpin);

int main()

{

   redLED = 1;

   greenLED = 1;

   while (true) {

       Led1(redLED);

       Led2(greenLED);

   }

}