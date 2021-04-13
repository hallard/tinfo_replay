#!/usr/bin/env python3

import serial
import time
import argparse

def record_file(file, port='/dev/ttyAMA0', baudrate=9600, bytes=2048, verbosity=1 ):
  print("Openning {} at {} bps for reading".format(port, baudrate))
  ser = serial.Serial(port, baudrate)
  while bytes >= 0:
    f = open(file, 'wb') 
    c = ser.read(1)
    # loop thru file bytes
    while c:
      # show on console if asked
      if verbosity > 0: 
        if c[0] != 0x02 and c[0] != 0x03:
          print(c.decode("ascii"), end='')
        else:
          print(c)
      # Send to serial
      f.write(c)
      f.flush();
      # read next
      c = ser.read(1)
      bytes = bytes -1
  f.close()

# /ain entry point
parser = argparse.ArgumentParser(description='Teleinfo frame reccorder')
parser.add_argument('-f', '--file', type=str, default='teleinfo.txt', help='teleinfo file name to reccord to')
parser.add_argument('-p', '--port', default='/dev/ttyAMA0',  type=str, help='serial port to read')
parser.add_argument('-b','--baudrate', default=9600,  type=int, help='baud rate for serial read')
parser.add_argument('-B', '--bytes', default=2048, type=int, help='number of bytes to reccord')
parser.add_argument('-v','--verbosity', default=0, action='count',  help='display output')

args = parser.parse_args()

record_file(**args.__dict__)

