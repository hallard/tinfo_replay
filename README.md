# Teleinfo record and replay frames


Phyton script to replay teleinfo frames for testing

You already need to have a text file that you grabbed from a smart meter to be able to replay it. This is not described here because out this scope.


## Recording Usage 

Just look into the code, it's a tool I quickly made, and can't document everything I'm doing.

Run for example:
`./tinfo_record.py -p /dev/tty.usbserial-14230 -m historique`

This record 5 frames (default) into default file `teleinfo.txt`

`./tinfo_record.py -p /dev/tty.usbserial-14230 -m standard --frame 2 --file teleinfo_standard.txt`

This record 2 frames into file `teleinfo_standard.txt`

Here is the output:

```
Openning /dev/tty.usbserial-TINFO_1507 at 1200 bps and writing to file teleinfo.txt
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

Use `--help` switch 

```shell
$ ./tinfo_replay-help
usage: tinfo_replay.py [-h] [-f FILE] [-p PORT] [-m {historique,standard}] [-l]

Teleinfo frame replayer

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  teleinfo replay file name (default teleinfo.txt)
  -p PORT, --port PORT  serial port to replay on (default /dev/ttyAMA0)
  -m {historique,standard}, --mode {historique,standard}
                        force mode else tries to auto-detect
  -l, --loop            restart sending file when at the end

```

To replay for example the file `teleinfo.txt in historique mode just use:

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

Tip : You can omit the `-m` parameter, in this case the player will try to auto detect mode reading in the file as follow:

- If it find `ADCO` set mode historique
- If it find `ADSC` set mode standard

Example
`./tinfo_replay.py -p /dev/tty.usbserial-01C07B96 -f trames/stand_base_tri_short.txt`

Here is the output:

```
Autodetecting mode from trames/stand_base_tri_short.txt
Openning /dev/tty.usbserial-01C07B96 mode standard, waiting 0.9ms after each char
<STX><LF>ADSC<TAB>031776013513<TAB>2<CR>
<LF>VTIC<TAB>02<TAB>J<CR>
<LF>DATE<TAB>E210415200146<TAB><TAB>8<CR>
<LF>NGTF<TAB>      BASE      <TAB><<CR>
<LF>LTARF<TAB>      BASE      <TAB>F<CR>
<LF>EAST<TAB>027553175<TAB>2<CR>
<LF>EASF01<TAB>015643112<TAB>9<CR>
<LF>EASF02<TAB>009861893<TAB>O<CR>
<LF>EASF03<TAB>000826037<TAB>><CR>
<LF>EASF04<TAB>000514699<TAB>G<CR>
<LF>EASF05<TAB>000442412<TAB>7<CR>
<LF>EASF06<TAB>000265022<TAB>8<CR>
<LF>EASF07<TAB>000000000<TAB>(<CR>
<LF>EASF08<TAB>000000000<TAB>)<CR>
<LF>EASF09<TAB>000000000<TAB>*<CR>
<LF>EASF10<TAB>000000000<TAB>"<CR>
<LF>EASD01<TAB>010028696<TAB>@<CR>
<LF>EASD02<TAB>008310713<TAB>8<CR>
<LF>EASD03<TAB>002960408<TAB>?<CR>
<LF>EASD04<TAB>006253358<TAB>C<CR>
<LF>IRMS1<TAB>002<TAB>0<CR>
<LF>IRMS2<TAB>001<TAB>0<CR>
<LF>IRMS3<TAB>002<TAB>2<CR>
<LF>URMS1<TAB>234<TAB>C<CR>
<LF>URMS2<TAB>240<TAB>A<CR>
<LF>URMS3<TAB>231<TAB>B<CR>
<LF>PREF<TAB>12<TAB>B<CR>
<LF>PCOUP<TAB>12<TAB>\<CR>
<LF>SINSTS<TAB>01198<TAB>Y<CR>
<LF>SINSTS1<TAB>00497<TAB>K<CR>
<LF>SINSTS2<TAB>00299<TAB>L<CR>
<LF>SINSTS3<TAB>00402<TAB>?<CR>
<LF>SMAXSN<TAB>E210415081021<TAB>07337<TAB>7<CR>
<LF>SMAXSN1<TAB>E210415052715<TAB>02892<TAB>1<CR>
<LF>SMAXSN2<TAB>E210415080748<TAB>02787<TAB><<CR>
<LF>SMAXSN3<TAB>E210415161727<TAB>02762<TAB>3<CR>
<LF>SMAXSN-1<TAB>E210414032733<TAB>05487<TAB>^<CR>
<LF>SMAXSN1-1<TAB>E210414052143<TAB>02196<TAB>F<CR>
<LF>SMAXSN2-1<TAB>E210414032614<TAB>01803<TAB>B<CR>
<LF>SMAXSN3-1<TAB>E210414114344<TAB>02561<TAB>F<CR>
<LF>CCASN<TAB>E210415200000<TAB>00750<TAB>3<CR>
<LF>CCASN-1<TAB>E210415193000<TAB>02490<TAB>_<CR>
<LF>UMOY1<TAB>E210415200000<TAB>232<TAB>!<CR>
<LF>UMOY2<TAB>E210415200000<TAB>239<TAB>)<CR>
<LF>UMOY3<TAB>E210415200000<TAB>236<TAB>'<CR>
<LF>STGE<TAB>003A4001<TAB>><CR>
<LF>MSG1<TAB>PAS DE          MESSAGE         <TAB><<CR>
<LF>PRM<TAB>25203473204149<TAB>/<CR>
<LF>RELAIS<TAB>000<TAB>B<CR>
<LF>NTARF<TAB>01<TAB>N<CR>
<LF>NJOURF<TAB>00<TAB>&<CR>
<LF>NJOURF+1<TAB>00<TAB>B<CR>
<LF>PJOURF+1<TAB>00008001 NONUTILE NONUTILE NONUTILE NONUTILE NONUTILE NONUTILE NONUTILE NONUTILE NONUTILE NONUTILE<TAB>9<CR>
<ETX>
```


