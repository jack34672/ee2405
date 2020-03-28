#include "mbed.h"

Serial pc( USBTX, USBRX );
AnalogOut Aout(DAC0_OUT);
AnalogIn Ain(A0);
DigitalIn  Switch(SW3);

BusOut display(D6, D7, D9, D10, D11, D5, D4, D8);

char table[10] = {0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F};

int sample = 1001;
int i;

float ADCdata[1001];

int main(){
  int count = 0;
  for (i = 1; i < sample; i++){
    Aout = Ain;
    ADCdata[i] = Ain;
    wait(1./sample);
    // wait(0.02);
    if(ADCdata[i-1] <= 0.1){
        if(ADCdata[i] > 0.1){
            count++ ;
        }
    }
  }

  for (i = 0; i < sample; i++){
    pc.printf("%1.3f\r\n", ADCdata[i]);
    wait(0.1);
  }

  count = count - count/100*7 ;

    float j;

  while(1){
    if( Switch == 0 ){
        display = table[(count / 100) % 10];
        wait(1.0);
        display = table[(count / 10) % 10];
        wait(1.0);
        display = table[count % 10];
        wait(1.0);
    }
    if( Switch == 1 ){
        display  = 0x00;
        for( j=0; j<2; j+=0.05 ){
            Aout = 0.5 + 0.5*sin(j*3.14159);
            wait(1./count/40);
        }
    }
  }
}