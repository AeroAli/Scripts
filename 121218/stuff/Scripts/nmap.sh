nmap -sT -p1-65535 -v -v -T4 -sV -O -oA TCP65535 -iL hostList.txt
nmap -sU -p1-65535 -v -v –T4 -sV -oA UDP65535 -iL hostList.txt
nmap -sT -p1-500 -v -v -T4 -sV -oA TCP500 -iL hostList.txt
nmap -sU -p1-500 -v -v –T4 -sV -oA UDP500 -iL hostList.txt
nmap -sT -p80 -v -v -T4 -sV -oA TCP80 -iL hostList.txt
nmap -sU -p80 -v -v –T4 -sV -oA UDP80 -iL hostList.txt
