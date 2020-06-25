#include "mbed.h"
#include "arm_math.h"
#include "FXOS8700CQ.h"
#include "bbcar.h"
#include <math.h>
#include <stdlib.h>

Ticker servo_ticker;
Ticker encoder_ticker_left;
Ticker encoder_ticker_right;

PwmOut pin8(D8), pin9(D9);
DigitalIn pin3(D3);
DigitalIn pin4(D4);

#define bound 0.9

BBCar car(pin8, pin9, servo_ticker);
FXOS8700CQ acc(PTD9, PTD8, (0x1D<<1));
DigitalInOut ping(D13);
DigitalOut redLED(LED1);

float state[3] = {0};
float Kp = 0, Ki = 0, Kd = 0;
float a0 = 0, a1 = 0, a2 = 0;

void pid_init(){
    state[0] = 0;
    state[1] = 0;
    state[2] = 0;

    a0 = Kp + Ki + Kd;
    a1 = (-Kp) - 2*Kd;
    a2 = Kd;
}

float pid_process(float in){

    int out = in*a0 + a1*state[0] + a2*state[1] + state[2];

    //update state
    state[1] = state[0];
    state[0] = in;
    state[2] = out;

    return out;
}


int main() {

    parallax_encoder encoder0(pin4, encoder_ticker_left);
    parallax_encoder encoder1(pin3, encoder_ticker_right);
    encoder0.reset();
    encoder1.reset();    

    car.goStraight(100);
    while(encoder1.get_cm()<80) wait_ms(50);
    car.stop();
    //rotate(90,'r');

    car.turn(100,-0.1);
    encoder1.reset();
    while(encoder1.get_cm()<10.2*2*PI/4) wait_ms(50);
    car.stop();

    encoder1.reset();
    car.goStraight(100);
    while(encoder1.get_cm()<100) wait_ms(50);
    car.stop();

    car.turn(-100,-0.1);
    encoder1.reset();
    while(encoder1.get_cm()<10.2*2*PI/4) wait_ms(50);
    car.stop();

    encoder1.reset();
    car.goStraight(-100);
    while(encoder1.get_cm()<30) wait_ms(50);
    car.stop();

    wait_ms(1000);

    encoder1.reset();
    car.goStraight(100);
    while(encoder1.get_cm()<30) wait_ms(50);
    car.stop();

    car.turn(100,0.1);
    encoder0.reset();
    while(encoder0.get_cm()<10.2*2*PI/4) wait_ms(50);
    car.stop();

    encoder1.reset();
    car.goStraight(100);
    while(encoder1.get_cm()<70) wait_ms(50);
    car.stop();

    car.turn(100,0.1);
    encoder0.reset();
    while(encoder0.get_cm()<10.2*2*PI/4) wait_ms(50);
    car.stop();

    encoder1.reset();
    car.goStraight(100);
    while(encoder1.get_cm()<100) wait_ms(50);
    car.stop();

////////// MISSION 2 ///////////////////

    car.turn(100,0.1);
    encoder0.reset();
    while(encoder0.get_cm()<10.2*2*PI/4) wait_ms(50);
    car.stop();

    encoder1.reset();
    car.goStraight(100);
    while(encoder1.get_cm()<25) wait_ms(50);
    car.stop();

    car.turn(100,0.1);
    encoder0.reset();
    while(encoder0.get_cm()<10.2*2*PI/4) wait_ms(50);
    car.stop();

    int find = 0;
    int loop = 0;
    int i;        
    ping.input();
    float distance[5];
    
    while ((find == 0) && (loop < 3)) {
        for (i = 0; i < 5; i++) {
            encoder1.reset();
            car.goStraight(100);
            while(encoder1.get_cm()<45) wait_ms(50);
            car.stop();

            wait_ms(500);
            distance[i] = ping.read();

            encoder1.reset();
            car.goStraight(-100);
            while(encoder1.get_cm()<25) wait_ms(50);
            car.stop();

            car.turn(-100,-0.1);
            encoder1.reset();
            while(encoder1.get_cm()<5*2*PI/4) wait_ms(50);
            car.stop();

            encoder1.reset();
            car.goStraight(-100);
            while(encoder1.get_cm()<15) wait_ms(50);
            car.stop();

            car.turn(-100,0.1);
            encoder0.reset();
            while(encoder0.get_cm()<5*2*PI/4) wait_ms(50);
            car.stop();
        }
        if ((distance[0] - distance[1] > 0) && (distance[1] - distance[2] > 0) && (distance[2] - distance[3] > 0) && (distance[3] - distance[4] > 0)) {
            find = 1;
            redLED = 1;
        }
    }
    car.turn(-100,0.1);
    encoder0.reset();
    while(encoder0.get_cm()<10.2*2*PI/4) wait_ms(50);
    car.stop();

    encoder1.reset();
    car.goStraight(100);
    while(encoder1.get_cm()<50) wait_ms(50);
    car.stop();

    car.turn(100,0.1);
    encoder0.reset();
    while(encoder0.get_cm()<10.2*2*PI/4) wait_ms(50);
    car.stop();

    encoder1.reset();
    car.goStraight(100);
    while(encoder1.get_cm()<150) wait_ms(50);
    car.stop();

}