# Teleinfo reccord and replay frames


Phyton script to replay teleinfo frames for testing

You already need to have a text file that you grabbed from a smart meter to be able to replay it. This is not described here because out this scope.


## Rccord Usage 

Just look into the code, it's a tool I quickly made, and can't document everything I'm doing.

Run for example:
`./tinfo_reccord.py -p /dev/tty.usbserial-14230 -m historique`

This reccord 5 frames (default) into default file `teleinfo.txt`

`./tinfo_reccord.py -p /dev/tty.usbserial-14230 -m standard --frame 2 --file teleinfo_standard.txt`

This reccord 2 frames into file `teleinfo_standard.txt`

Here is the output:

```
Openning /dev/tty.usbserial-TINFO_1507 at 1200 bps and wrtiting to file teleinfo.txt
Waiting end of frame
<STX><LF>ADCO 021528603314 :<CR>
<LF>OPTARIF HC.. <<CR>
<LF>ISOUSC 15 <<CR>
<LF>HCHC 000837362 #<CR>
<LF>HCHP 002035822 )<CR>
<LF>PTEC HP..  <CR>
<LF>IINST 001 X<CR>
<LF>IMAX 002 A<CR>
<LF>PAPP 00200 #<CR>
<LF>HHPHC A ,<CR>
<LF>MOTDETAT 000000 B<CR>
<ETX><STX><LF>ADCO 021528603314 :<CR>
<LF>OPTARIF HC.. <<CR>
<LF>ISOUSC 15 <<CR>
<LF>HCHC 000837362 #<CR>
<LF>HCHP 002035822 )<CR>
<LF>PTEC HP..  <CR>
<LF>IINST 001 X<CR>
<LF>IMAX 002 A<CR>
<LF>PAPP 00190 +<CR>
<LF>HHPHC A ,<CR>
<LF>MOTDETAT 000000 B<CR>
<ETX>
```

## Replay Usage 

To replay for example the file teleinfo.txt in legacy mode just use: 
`./tinfo_replay.py -p /dev/tty.usbserial-TINFO_1507 -m historique`


Here is the output:

```
Openning /dev/tty.usbserial-TINFO_1507 mode historique, waiting 7.5ms after each char
<STX><LF>ADCO 021528603314 :<CR>
<LF>OPTARIF HC.. <<CR>
<LF>ISOUSC 15 <<CR>
<LF>HCHC 000837362 #<CR>
<LF>HCHP 002035822 )<CR>
<LF>PTEC HP..  <CR>
<LF>IINST 001 X<CR>
<LF>IMAX 002 A<CR>
<LF>PAPP 00200 #<CR>
<LF>HHPHC A ,<CR>
<LF>MOTDETAT 000000 B<CR>
<ETX><STX><LF>ADCO 021528603314 :<CR>
<LF>OPTARIF HC.. <<CR>
<LF>ISOUSC 15 <<CR>
<LF>HCHC 000837362 #<CR>
<LF>HCHP 002035822 )<CR>
<LF>PTEC HP..  <CR>
<LF>IINST 001 X<CR>
<LF>IMAX 002 A<CR>
<LF>PAPP 00190 +<CR>
<LF>HHPHC A ,<CR>
<LF>MOTDETAT 000000 B<CR>
<ETX>charles@mac-office:tinfo_replay$ 

```


