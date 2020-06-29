import paho.mqtt.client as paho

import time

import serial

import locale

import threading
import csv
mqttc = paho.Client()

# Settings for connection

host = "192.168.1.113"

topic= "velocity"

port = 1883


# Callbacks

def on_connect(self, mosq, obj, rc):

    print("Connected rc: " + str(rc))


def on_message(mosq, obj, msg):

    print("[Received] Topic: " + msg.topic + ", Message: " + str(msg.payload) + "\n")


def on_subscribe(mosq, obj, mid, granted_qos):

    print("Subscribed OK")


def on_unsubscribe(mosq, obj, mid, granted_qos):

    print("Unsubscribed OK")


# Set callbacks

mqttc.on_message = on_message

mqttc.on_connect = on_connect

mqttc.on_subscribe = on_subscribe

mqttc.on_unsubscribe = on_unsubscribe


# Connect and subscribe

print("Connecting to " + host + "/" + topic)

#mqttc.connect(host, port=1883, keepalive=60)

#mqttc.subscribe(topic, 0)

serdev = '/dev/ttyUSB0'

s = serial.Serial(serdev, 9600)

print("start")



x=[]
with open('log.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    while(1):

        line=s.read(1)

        x=line.decode()

        x=locale.atoi(x)

        #mqttc.publish(topic, x)

        print(x)
        localtime = time.asctime( time.localtime(time.time()) )
        #mqttc.loop()
        writer.writerow([localtime, x])
        time.sleep(0.1)