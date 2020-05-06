import numpy as np

import serial

import time


waitTime = 0.1


# generate the waveform table



song =np.array(
[
  261, 261, 392, 392, 440, 440, 392,

  349, 349, 330, 330, 294, 294, 261,

  392, 392, 349, 349, 330, 330, 294,

  392, 392, 349, 349, 330, 330, 294,

  261, 261, 392, 392, 440, 440, 392,

  349, 349, 330, 330, 294, 294, 261
]

)

song2 =np.array(
[
  261, 261, 294, 261, 349, 330,

  261, 261, 294, 261, 392, 349,

  261, 261, 523, 440, 349, 330,

  349, 349, 330, 261, 294, 261

]

)

song = song /499
song2 = song2 /499

# output formatter
print(song)
print(song2)

a = 1

formatter = lambda x: "%.3f" % x


# send the waveform table to K66F

serdev = '/dev/ttyACM0'

s = serial.Serial(serdev)

while(1):
    b = s.readline()
    print(b[0])
    if(b[0] == 48):
      print("Sending signal ...")

      print("It may take about  seconds ..." )

      for data in song:
          s.write(bytes(formatter(data), 'UTF-8'))
          time.sleep(waitTime)

          #s.close()

      print("Signal sended")
    if(b[0] == 49):
      print("Sending signal ...")

      print("It may take about  seconds ..." )

      for data in song2:
          s.write(bytes(formatter(data), 'UTF-8'))
          time.sleep(waitTime)

          #s.close()

      print("Signal sended")
    
