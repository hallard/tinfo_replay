#!/usr/bin/env python3

import serial
import time
import argparse

def replay_file(fname, port='/dev/ttyAMA0', baudrate=9600, loop=True, verbosity=1 ):
  # Open Serial Port as binary (do not touch anything)
  dev = serial.Serial(port, baudrate)
  file = open(fname, 'rb') 
  c = file.read(1)
  # loop thru file bytes
  while c:
    # show on console if asked
    if verbosity > 0: 
      if c[0] != 0x02 and c[0] != 0x03:
        print(c.decode("ascii"), end='')
      else:
        print(c)
    # Send to serial
    dev.write(c)
    # read next
    c = file.read(1)

# /ain entry point
parser = argparse.ArgumentParser(description='Teleinfo frame replayer')
parser.add_argument('fname', metavar='filename', type=str, help='teleinfo replay file name')
parser.add_argument('-p', '--port', default='/dev/ttyAMA0',  type=str, help='serial port to replay on')
parser.add_argument('-b','--baudrate', default=9600,  type=int, help='baud rate for serial replay')
parser.add_argument('-L', '--loop', default=True, action='store_true',  help='whether to loop indefinitely')
parser.add_argument('-v','--verbosity', default=0, action='count',  help='display output')

args = parser.parse_args()

replay_file(**args.__dict__)

