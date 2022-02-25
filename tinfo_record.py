#! /usr/bin/env python3

import serial
import time
import argparse
import socket

def record_file(file, port='/dev/ttyAMA0',mode='standard', frame=5 ):
  baudrate = 9600
  if mode == 'historique':
    baudrate = 1200
  if port[0]=="/":
    print(f"Openning {port} at {baudrate} bps and writing to file {file}")
    ser = serial.Serial(port, baudrate,  parity=serial.PARITY_EVEN, bytesize=serial.SEVENBITS)
    getChar = lambda n : ser.read(n)
  else:
    addr = port.split(':')
    print(f"Openning {addr[0]}:{addr[1]} at {baudrate} bps and writing to file {file}")
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.connect((addr[0],int(addr[1])))
    getChar = lambda n : tcp.recv(n)
  f = open(file, 'wb')
  # avoid garbage at startup
  for x in range(16):
    getChar(1)

  print("Waiting end of frame")
  while getChar(1)[0]!=0x03:
    pass

  fullframe = False
  # loop thru serial
  while frame or fullframe==False:
    c = getChar(1)
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
parser = argparse.ArgumentParser(description='Teleinfo frame recorder')
parser.add_argument('-f', '--file', type=str, default='teleinfo.txt', help='teleinfo file name to record to')
parser.add_argument('-p', '--port', default='/dev/ttyAMA0',  type=str, help='serial port to read')
parser.add_argument('-m','--mode', choices=['historique', 'standard'], default='standard', type=str, help='mode, historique or standard')
parser.add_argument('-F', '--frame', default=5, type=int, help='number of frame to record')

args = parser.parse_args()
record_file(**args.__dict__)
