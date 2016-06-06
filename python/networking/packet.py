#!/usr/bin/python3

import pcapy
from struct import *

cap=pcapy.open_live("ens33",65536,1,0)

while True:
    try:
        (header,payload)=cap.next()
    except Exception:
        continue
    l2hdr=payload[:14]
    l2data=unpack("!6s6sH",l2hdr)
    print(l2data)
