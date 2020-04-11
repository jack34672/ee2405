import matplotlib.pyplot as plt
import numpy as np
import serial
import time

t = np.arange(0,10,0.1) 
X = np.arange(0,10,0.1) 
Y = np.arange(0,10,0.1) 
Z = np.arange(0,10,0.1)
tilt = np.arange(0,10,0.1) 

serdev = '/dev/ttyACM0'
s = serial.Serial(serdev,115200)

for x in range(0, 100):

    line=s.readline() # Read an echo string from K66F terminated with '\n'
    line2=s.readline() # Read an echo string from K66F terminated with '\n'
    line3=s.readline() # Read an echo string from K66F terminated with '\n'
    line4=s.readline() # Read an echo string from K66F terminated with '\n'

    # print line

    X[x] = float(line)
    Y[x] = float(line2)
    Z[x] = float(line3)
    tilt[x] = float(line4)

fig, ax = plt.subplots(2, 1)
l1,=ax[0].plot(t,X)
l2,=ax[0].plot(t,Y)
l3,=ax[0].plot(t,Z)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Acc Vector')
ax[0].legend((l1,l2,l3),('X','Y','Z'))
ax[1].stem(t,tilt,'b') 
ax[1].set_xlabel('Time')
ax[1].set_ylabel('Tilt')
plt.show()
s.close()