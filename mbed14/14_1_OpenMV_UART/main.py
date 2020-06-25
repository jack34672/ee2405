import pyb
import sensor, image, time, os, tf

uart = pyb.UART(3,9600,timeout_char=1000)
uart.init(9600,bits=8,parity = None, stop=1, timeout_char=1000)
tmp = ""

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False) # must turn this off to prevent image washout...
clock = time.clock()

while(True):
   clock.tick()
   out=[]
   a = uart.readline()

   if a is not None:
      tmp += a.decode()
      print(a.decode())

   if tmp == "image_classification":
      print("classify images")
      tmp =""
      while(True):
          img = sensor.snapshot()
          img.lens_corr(1.8) # strength of 1.8 is good for the 2.8mm lens.
          for code in img.find_qrcodes():
            img.draw_rectangle(code.rect(), color = (255, 0, 0))
            out+=code.payload()
            #print(code)
          if(out!=[]):
            break
      print(out[0])
      print(out[1])
      uart.write(str(out[0]).encode())
      uart.write(str(out[1]).encode())
      uart.write(str(out[2]).encode())
      uart.write(str(out[3]).encode())
      uart.write(str(out[4]).encode())
      print(str(out[0]).encode())
      print(str(out[1]).encode())
      print(str(out[2]).encode())
      print(str(out[3]).encode())
      print(str(out[4]).encode())

      print(clock.fps())