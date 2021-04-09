# PicoCTF2021 | Transformation

By [fatihsencer](https://github.com/fatihsencer)

## Description
I wonder what this really is... enc ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

## Analysis
We got a crypted text. When we look at the description we see how it is encrypted. First index is do bitwise operation (2^8) after convert to 'ascii value'. After that, ascii value of the next index add to first value. This encryption is applied every 2 indexes.

## Solution
Firstly, we get the ascii value of the letters in the file. 

```
crypted = [28777, 25455, 17236, 18043, 12598, 24418, 26996, 29535, 26990, 29556, 13108, 25695, 28518, 24376, 24368, SECRET, SECRET, SECRET, SECRET]
```

Now we can reverse bitwise operation. 

```
for x in range(0,len(crypted)):

    print(chr(int(crypted[x]/(2**8))),end='')
    
-> -> pcCF1_isis3do__SECRET
```

We found! No,wait.. Something seems wrong. 0,2,4,6... where is odd indexes?

Odd index is hidden in even index. Let's find odd index.

Step 1 -> bitwise operation to ascii value of first index ('p'). 

```
asci_value = ord(chr(int(crypted[x]/(2**8)))
```
Step 2 -> subtract ascii_value from first crypted index. After, convert char.

```
chr(crpyted[0]-ascii_value)
```

We get flag.

*Flag is: picoCTF{16_bits_inst34d_of_8_SECRET}*
