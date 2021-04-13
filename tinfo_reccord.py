#!/usr/bin/env python3

import serial
import time
import argparse

def record_file(file, port='/dev/ttyAMA0', baudrate=9600, frame=5 ):
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
    # show on console if asked
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
parser.add_argument('-b','--baudrate', default=9600,  type=int, help='baud rate for serial read')
parser.add_argument('-F', '--frame', default=5, type=int, help='number of frame to reccord')

args = parser.parse_args()
record_file(**args.__dict__)
