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


X = np.arange(0,1000,1) 
Y = np.arange(0,1000,1) 
Z = np.arange(0,1000,1)
tilt = np.arange(0,1000,1) 

i = 0
s.write("/getAcc/run\r".encode())
time.sleep(0.5)
s.write("/getAcc/run\r".encode())
time.sleep(0.5)
line=s.read(1)
while True:
    # send RPC to remote
    s.write("/getAcc/run\r".encode())
    line=s.readline() # Read an echo string from K66F terminated with '\n'
    tilt[i] = int(line)
    print(tilt[i])
    if tilt[i] == 1:
        time.sleep(0.1)
        for x in range(10):
            i = i + 1
            s.write("/getAcc/run\r".encode())
            line=s.readline() # Read an echo string from K66F terminated with '\n'
            tilt[i] = float(line)
            print(tilt[i])
            time.sleep(0.1)
    time.sleep(0.5)
    i = i + 1
s.close()

fig, ax = plt.subplots(2, 1)
l1,=ax[0].plot(t[0:i],X[0:i])
l2,=ax[0].plot(t[0:i],Y[0:i])
l3,=ax[0].plot(t[0:i],Z[0:i])
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Acc Vector')
ax[0].legend((l1,l2,l3),('X','Y','Z'))
ax[1].stem(t[0:i],tilt[0:i],'b') 
ax[1].set_xlabel('Time')
ax[1].set_ylabel('Tilt')
plt.show()
s.close()