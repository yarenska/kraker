import sys
from scapy.all import *

ip = IP(dst='10.471.52.38')
# IP address of the destination

open_ports = []


for portnum in range(65535):

    syn = TCP(sport=RandShort(), dport=portnum, flags='S')
    synack = sr1(ip/syn, verbose=False)
    print '[*]Scanning port for TCP {}'.format(portnum)
    fl = str(synack[TCP].flags)

    if fl == '20':
        continue
    elif fl == '18':
        print '[+]{} # port is open.'.format(portnum)
        open_ports.append(portnum)


for portnum in range(65535):

    udp = UDP(sport=RandShort(), dport=portnum)
    udp_resp = sr1(ip/udp, verbose=False, timeout=0.1)
    print '[*]Scanning port for UDP {}'.format(portnum)
    if udp_resp:
        if udp_resp.haslayer(UDP):
            print '[+]{} # port is open.'.format(portnum)
            open_ports.append(portnum)
        else:
            code = str(usp_resp[ICMP].code)
            typ = str(udp_resp[ICMP].type)

            if code == '3' and typ == '3': #PORT IS UNREACHABLE
                pass
    else:
            print '[+]{} #port may or may not be open.'.format(portnum)

for portnum in open_ports:
    print '[+]{} # port is open.'.format(portnum)
