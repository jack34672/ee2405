import serial
import time
import matplotlib.pyplot as plt
import numpy as np

# XBee setting
serdev = '/dev/ttyUSB0'
s = serial.Serial(serdev, 9600)

s.write("+++".encode())
char = s.read(2)
print("Enter AT mode.")
print(char.decode())

s.write("ATMY 0x140\r\n".encode())
char = s.read(3)
print("Set MY 0x140.")
print(char.decode())

s.write("ATDL 0x240\r\n".encode())
char = s.read(3)
print("Set DL 0x240.")
print(char.decode())
s.write("ATID 0x1\r\n".encode())
char = s.read(3)
print("Set PAN ID 0x1.")
print(char.decode())

s.write("ATWR\r\n".encode())
char = s.read(3)
print("Write config.")
print(char.decode())

s.write("ATMY\r\n".encode())
char = s.read(4)
print("MY :")
print(char.decode())

s.write("ATDL\r\n".encode())
char = s.read(4)
print("DL : ")
print(char.decode())

s.write("ATCN\r\n".encode())
char = s.read(3)
print("Exit AT mode.")
print(char.decode())

print("start sending RPC")
a=bytes("\r", 'UTF-8')
b=bytes("/getAcc/run\r", 'UTF-8')
c=bytes("/getAddr/run\r", 'UTF-8')


tilt = np.arange(0,1000,1) 

import paho.mqtt.client as paho
import time

# https://os.mbed.com/teams/mqtt/wiki/Using-MQTT#python-client

# MQTT broker hosted on local machine
mqttc = paho.Client()

# Settings for connection
# TODO: revise host to your ip
host = "172.16.225.90"
topic = "velocity"

# Callbacks
def on_connect(self, mosq, obj, rc):
      print("Connected rc: " + str(rc))

def on_message(mosq, obj, msg):
      print("[Received] Topic: " + msg.topic + ", Message: " + str(msg.payload) + "\n");

def on_subscribe(mosq, obj, mid, granted_qos):
      print("Subscribed OK")

def on_unsubscribe(mosq, obj, mid, granted_qos):
      print("Unsubscribed OK")


i = 0
last = 0
first = 1
# s.write("/getAcc/run\r".encode())
# time.sleep(0.5)
# s.write("/getAcc/run\r".encode())
# time.sleep(0.5)
# line=s.read(1)
while last == 0:
    # send RPC to remote
    s.write("/getAcc/run\r".encode())
    line = s.readline().decode() # Read an echo string from K66F terminated with '\n'
    if line[0:4] != "/get": 
        et = mqttc.publish(topic, line, qos=0)
        print(line)

    # tilt[i] = int(line)
    # print(tilt[i])
    # i = i + 1
    # if line == '/getAcc/run\r\n':
    #     print(line)
    #     last = 1
    time.sleep(0.5)

mqttc.loop_forever()
s.close()

