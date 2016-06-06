#!/usr/bin/python3

import socket
import struct
import textwrap

def main():
    conn = socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.ntohs(3))
    while True:
        raw_data,addr = conn.recvfrom(65536)
        dest_mac,src_mac,proto,payload = ethernet_frame(raw_data)
        print("\n Ethernet frame:")
        print("Destination Mac:{},Source Mac:{},Protocol:{}".format(dest_mac,src_mac,proto))

def ethernet_frame(data):
    dest_mac,src_mac,proto = struct.unpack('!6s6sH',data[:14])
    return getmac_addr(dest_mac),getmac_addr(src_mac),socket.htons(3),data[14:]

def getmac_addr(bytes_addr):
    bytes_str = map("{:02x}".format,bytes_addr)
    return ":".join(bytes_str).upper()

def Ipv4_packet(data):
    ipversion_headerlength = data[0]
    ipversion = ipversion_headerlength >> 4
    header_length = (ipversion_headerlength & 15) * 4
    ttl,proto,src,dest = struct.unpack("! 8x B B 2x 4s 4s",data[:20])
    return ipversion, header_length, ttl, proto, getip(src), getip(dest)

def getip(addr):
    return '.'.join(map(str,addr))

#unpack a imcp packet
def icmp_unpack(data):
    imcp_type,code,checksum = struct.unpack("! B B H",data[:4])
    return icmp_type,code,checksum,data[4:]

#unpack a tcp packet
def tcp_packet(data):
    sport,dport,seq_num,ack_num,offset_flags = struct.unpack('! H H L L H',data[:14])
    offset = (offset_flags >> 12) * 4
    flag_urg = (offset_flags >> 32) * 5
    flag_ack = (offset_flags >> 16) * 4
    flag_psh = (offset_flags >> 8) * 3
    flag_rst = (offset_flags >> 4) * 2
    flag_syn = (offset_flags >> 2) * 1
    flag_fin = (offset_flags >> 1)
    return sport,dport,seq_num,ack_num,offset,flag_urg,flag_ack,flag_psh,flag_rst,flag_syn,flag_fin,data[14:]


main()
