from http.client import HTTPResponse
from time import process_time
import scapy.all as scapy
from scapy.layers import http
import data


import Server


def sniffing(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packet)


def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        # print(packet[http.HTTPRequest].Host)
        data.store_data(packet[http.HTTPRequest].Host)
        Server.server_code()
        # print(packet)


sniffing("Wi-Fi")
# print(data.host_list)
