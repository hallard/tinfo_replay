#!/usr/bin/env python3

import serial
import time
import argparse

def replay_file(file, port='/dev/ttyAMA0', mode='', loop=False):

  if mode == '':
    print("Autodetecting mode from {}".format(file))
    with open(file) as f:
      for line in f:
        if "ADCO" in line:
          mode = 'historique'
          break
        elif "ADSC" in line:
          mode = 'standard'
          break
      f.close()

  baudrate = 9600
  if mode == 'historique':
    baudrate = 1200
  
  # Avoid flooding serial and keep same as teleinfo speed
  # Start/Stop/7 bits/Parity = 10 bits total
  # remove 1 bits to be sure not slowing down process
  dly = ( 10 - 1) / baudrate  ;
  # Open Serial Port as binary (do not touch anything)
  print("Openning {} mode {}, waiting {:.1f}ms after each char".format(port, mode, dly*1000))
  dev = serial.Serial(port, baudrate, parity=serial.PARITY_EVEN, bytesize=serial.SEVENBITS)
  while True:
    f = open(file, 'rb') 
    c = f.read(1)
    # loop thru file bytes
    while c:
      # show on console if asked
      if c[0]==0x02:
        print("<STX>", end='')
      elif c[0]==0x03:
        print("<ETX>", end='')
      elif c[0]==0x09:
        print("<TAB>", end='')
      elif c[0]==0x0d:
        print("<CR>")
      elif c[0]==0x0a:
        print("<LF>", end='')
      else:
        print(c.decode("ascii"), end='')
      # Send to serial
      dev.write(c)
      time.sleep(dly)
      dev.flush();
      # read next
      c = f.read(1)
    f.close()

    if loop == False:
      break

# /ain entry point
parser = argparse.ArgumentParser(description='Teleinfo frame replayer')
parser.add_argument('-f', '--file', type=str, default='teleinfo.txt', help='teleinfo replay file name (default teleinfo.txt)')
parser.add_argument('-p', '--port', default='/dev/ttyAMA0', type=str, help='serial port to replay on (default /dev/ttyAMA0)')
parser.add_argument('-m','--mode', choices=['historique', 'standard'], default='', type=str, help='force mode else tries to auto-detect')
parser.add_argument('-l', '--loop', default=False, action='store_true',  help='restart sending file when at the end')

args = parser.parse_args()

replay_file(**args.__dict__)

