#!/usr/bin/env python3

import serial
import time
import argparse

def record_file(file, port='/dev/ttyAMA0',mode='standard', frame=5 ):
  baudrate = 9600
  if mode == 'historique':
    baudrate = 1200
  print("Openning {} at {} bps and wrtiting to file {}".format(port, baudrate, file))
  ser = serial.Serial(port, baudrate,  parity=serial.PARITY_EVEN, bytesize=serial.SEVENBITS)
  f = open(file, 'wb')
  # avoid garbage at startup
  for x in range(16):
    ser.read(1)

  print("Waiting end of frame")
  while ser.read(1)[0]!=0x03:
    pass

  fullframe = False
  # loop thru serial
  while frame or fullframe==False:
    c = ser.read(1)
    if c[0]==0x02:
      print("<STX>", end='')
      fullframe = False
    elif c[0]==0x03:
      print("<ETX>", end='')
      fullframe = True
      frame = frame -1
    elif c[0]==0x09:
      print("<TAB>", end='')
    elif c[0]==0x0d:
      print("<CR>")
    elif c[0]==0x0a:
      print("<LF>", end='')
    else:
      print(c.decode("ascii"), end='')
    # Send to file
    f.write(c)
    f.flush();

  f.close()

# /ain entry point
parser = argparse.ArgumentParser(description='Teleinfo frame reccorder')
parser.add_argument('-f', '--file', type=str, default='teleinfo.txt', help='teleinfo file name to reccord to')
parser.add_argument('-p', '--port', default='/dev/ttyAMA0',  type=str, help='serial port to read')
parser.add_argument('-m','--mode', choices=['historique', 'standard'], default='standard', type=str, help='mode, historique or standard')
parser.add_argument('-F', '--frame', default=5, type=int, help='number of frame to reccord')

args = parser.parse_args()
record_file(**args.__dict__)
