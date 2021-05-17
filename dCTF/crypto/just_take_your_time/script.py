#!/usr/bin/python3

from pwn import *
from re import *
from time import time
from Crypto.Cipher import DES3
from binascii import unhexlify
from secrets import token_hex

URL = "dctf-chall-just-take-your-time.westeurope.azurecontainer.io"
port = 9999

r = remote(URL,port)

################### Q1

r.recvuntil("second.").decode('utf-8')

text = r.recvuntil("=").decode('utf-8').strip().split(' ')

number1 = int(text[0])
number2 = int(text[2])

r.sendline(str(number1*number2))

################### Q2

key = str(int(time())).zfill(16).encode("utf-8")

r.recvuntil('be yours!\n')

encrypted = unhexlify(r.recvline().strip())
cipher = DES3.new(key, DES3.MODE_CFB, b"00000000")
decrypted = cipher.decrypt(encrypted)

r.sendline(decrypted)

r.recvuntil("flag.")

flag = r.recvall().strip().decode('utf-8')

print(flag)


