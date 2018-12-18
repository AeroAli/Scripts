masscan -p80,8000-8100 192.168.0.1 -oB masscan180T
masscan -p80,8000-8100 192.168.0.2 -oB masscan280T
masscan -p80,8000-8100 192.168.0.10 -oB masscan1080T
masscan -p80,8000-8100 192.168.0.11 -oB masscan1180T
masscan -p U:80,8000-8100 192.168.0.1 -oB masscan180U
masscan -p U:80,8000-8100 192.168.0.2 -oB masscan280U
masscan -p U:80,8000-8100 192.168.0.10 -oB masscan1080U
masscan -p U:80,8000-8100 192.168.0.11 -oB masscan1180U
masscan -p 1-1000 192.168.0.1 -oB masscan11000T
masscan -p 1-1000 192.168.0.2 -oB masscan21000T
masscan -p 1-1000 192.168.0.10 -oB masscan101000T
masscan -p 1-1000 192.168.0.11 -oB masscan111000T
masscan -p U:1-1000 192.168.0.1 -oB masscan11000U
masscan -p U:1-1000 192.168.0.2 -oB masscan21000U
masscan -p U:1-1000 192.168.0.10 -oB masscan101000U
masscan -p U:1-1000 192.168.0.11 -oB masscan111000U
masscan -p80 --banners 192.168.0.1  -oB masscan1Banners
masscan -p80 --banners 192.168.0.2  -oB masscan2Banners
masscan -p80 --banners 192.168.0.10  -oB masscan10Banners
masscan -p80 --banners 192.168.0.11  -oB masscan11Banners
