import os
import json
hosts = {}

def getIPs(fileName):
	with open(fileName) as f:
		for line in f:
			(key, val) = line.split()
			hosts[key] = val
	

def getPing():
	for ip in hosts:
		val = []
		os.system("ping -c 1 " + ip + " > output.txt")
		with open("output.txt") as f:
			for line in f:
				val.append(line)
		hosts[ip] = val[1]

def searchMap(searchKey, searchVal):
	for ip in hosts:
		if (searchKey in hosts):
			if (searchVal not in hosts[searchKey]):
				return "Host OK"
			hosts[searchKey] = "Host not available"
			return hosts[searchKey]

getIPs("hostList.txt")
getPing()
for ip in hosts:
	searchMap(ip, "Unreachable")
print(json.dumps(hosts, sort_keys = True))
for ip in hosts:
	if (hosts[ip] != "Host not available"):
		os.system("/usr/bin/nmap -sT -p1-65535 -v -v -T4 -sV -O -oN " + ip + "TCP " + ip + " > nmapTCP" + ip + ".txt")
		os.system("rm " + ip + "TCP")
		print("TCP complete")
		os.system("/usr/bin/nmap -sU -p1-500 -v -v -T4 -sV -oN " + ip + "UDP " + ip + " > nmapUDP" + ip +".txt")
		os.system("rm " + ip + "UDP")
		print("UDP complete")
		os.system("/usr/bin/dig host -t axfr uadtargetnet.com " + ip + " > dig" + ip + ".txt")