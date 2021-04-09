fp = open('enc','r').read()

crypted = []

for x in fp:
    crypted.append(int(ord(x)))

flag = []

for x in range(0,len(crypted)):

    ascii_val = int(crypted[x]/(2**8))
    flag.append(chr(ascii_val))
    flag.append(chr(crypted[x]-(ascii_val << 8)))

print(''.join(flag))