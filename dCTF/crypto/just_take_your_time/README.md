Bize verilen adresi nc ile dinledigimizde cok uzun 2 sayiyi 1-2 saniyede carpmamizi istiyordu. 

Manuel olarak yapamayacagim icin ilk challange'i script yazarak hallettim.

```python

URL = "dctf-chall-just-take-your-time.westeurope.azurecontainer.io"
port = 9999

r = remote(URL,port)

r.recvuntil("second.").decode('utf-8')

text = r.recvuntil("=").decode('utf-8').strip().split(' ')

number1 = int(text[0])
number2 = int(text[2])

r.sendline(str(number1*number2))

```

Bize ikinci challange'i veriyor. Bu challange'ta bize flag'in sifrelenmis halini veriyor.

Verilen python kodunda nasil sifrelendigini goruyoruz. Ayni sekilde decode ederek flag'e ulasiyoruz.
