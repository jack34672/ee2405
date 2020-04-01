#include "mbed.h"
#include "uLCD_4DGL.h"

uLCD_4DGL uLCD(D1, D0, D2);

int main()
{
      uLCD.printf("\n106061146\n"); //Default Green on black text
      uLCD.line(30, 30 , 30, 60, RED);
      uLCD.line(30, 60 , 60, 60, RED);
      uLCD.line(60, 60 , 60, 30, RED);
      uLCD.line(60, 30 , 30, 30, RED);

      wait(30);
}