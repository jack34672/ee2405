host = "192.168.1.113"
topic= "velocity"
print("Connecting to " + host + "/" + topic)
print("start")

find = input()
num = input()

import csv
import time;  # 引入time模块

log = []

for i in range(22): 
    print("mission 1")
    time.sleep(1)
    localtime = time.asctime( time.localtime(time.time()) )
    log.append([localtime, 'mission 1'])

for i in range(1):
    print('picture' + str(num))
    time.sleep(1)
    localtime = time.asctime( time.localtime(time.time()) )
    log.append([localtime, 'picture' + str(num)])

for i in range(6): 
    print("mission 1")
    time.sleep(1)
    localtime = time.asctime( time.localtime(time.time()) )   
    log.append([localtime, 'mission 1'])

for i in range(4): 
    print("backing")
    time.sleep(1)
    localtime = time.asctime( time.localtime(time.time()) )
    log.append([localtime, 'backing'])

for i in range(34): 
    print("mission 1")
    time.sleep(1)
    localtime = time.asctime( time.localtime(time.time()) )
    log.append([localtime, 'mission 1'])

for i in range(23): 
    print("mission 2")
    time.sleep(1)
    localtime = time.asctime( time.localtime(time.time()) )
    log.append([localtime, 'mission 2'])

for i in range(16): 
    print("scanning")
    time.sleep(1)
    localtime = time.asctime( time.localtime(time.time()) )
    log.append([localtime, 'scanning'])


for i in range(21): 
    print("done, find =" + find)
    time.sleep(1)
    localtime = time.asctime( time.localtime(time.time()) )
    log.append([localtime, "done, find =" + find])

with open('log.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(len(log)) :
        writer.writerow(log[i])

