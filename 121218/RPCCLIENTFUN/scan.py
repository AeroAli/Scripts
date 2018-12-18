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
		os.mkdir("Results/" + ip)
		os.system("/usr/bin/rpcclient  " + ip + " -A creds.txt -c srvinfo > Results/" + ip + "/rpcclientS.txt")
		os.system("/usr/bin/rpcclient  " + ip + " -A creds.txt -c querydominfo > Results/" + ip + "/rpcclientDomInfo.txt")
		os.system("/usr/bin/rpcclient  " + ip + " -A creds.txt -c enumprocs > Results/" + ip + "/rpcclientProcs.txt")
		os.system("/usr/bin/rpcclient  " + ip + " -A creds.txt -c enumdrivers > Results/" + ip + "/rpcclientDrivers.txt")
		os.system("/usr/bin/rpcclient  " + ip + " -A creds.txt -c enumports > Results/" + ip + "/rpcclientPorts.txt")
		os.system("/usr/bin/rpcclient  " + ip + " -A creds.txt -c enumtrust > Results/" + ip + "/rpcclientTrust.txt")
		os.system("/usr/bin/rpcclient  " + ip + " -A creds.txt -c enumprinters > Results/" + ip + "/rpcclientPrinters.txt")
		os.system("/usr/bin/rpcclient  " + ip + " -A creds.txt -c enumprivs > Results/" + ip + "/rpcclientPrivs.txt")
		os.system("/usr/bin/rpcclient  " + ip + " -A creds.txt -c enumprocdatatypes > Results/" + ip + "/rpcclientProcDataTypes.txt")
		os.system("/usr/bin/rpcclient  " + ip + " -A creds.txt -c enummonitors > Results/" + ip + "/rpcclientMonitors.txt")
		os.system("/usr/bin/rpcclient  " + ip + " -A creds.txt -c enumalsgroups domain > Results/" + ip + "/rpcclientGroupDomain.txt")
		os.system("/usr/bin/rpcclient  " + ip + " -A creds.txt -c enumalsgroups builtin > Results/" + ip + "/rpcclientDroupBuiltin.txt")
		os.system("/usr/bin/rpcclient  " + ip + " -A creds.txt -c enumdomains > Results/" + ip + "/rpcclientDomain.txt")
		os.system("/usr/bin/rpcclient  " + ip + " -A creds.txt -c enumdomgroups > Results/" + ip + "/rpcclientDomGroups.txt")
		os.system("/usr/bin/rpcclient  " + ip + " -A creds.txt -c enumdomusers > Results/" + ip + "/rpcclientDomUsers.txt")
		print("rpcclient complete")
		print(ip + " complete")
		#rpcclient with enum results

