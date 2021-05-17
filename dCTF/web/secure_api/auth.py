#!/usr/bin/python3

import requests as r

data = { 
    "username":"guest",
    "password":"guest"
}

req_post = r.post("http://dctf1-chall-secure-api.westeurope.azurecontainer.io:8080/login", data=data)

print(req_post.text)
