# PicoCTF2021 | Transformation

By [fatihsencer](https://github.com/fatihsencer)

## Description
I wonder what this really is... enc ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

## Analysis
We got a crypted text. When we look at the description we see how it is encrypted. First index converting to 'ascii value' and do bitwise operation (2^8). After that, value of the next index ascii value add first value.

## Solution
We got a crypted text. When we look at the description we see how it is encrypted. Firstly, first index converting to 'ascii value' and bitwise operation.
First thing, i tried to do a "strings" on the file to see if the flag in the raw data.
```
strings chall.png | grep -i shaktictf
```
But their wasn't anything.
Second try, i looked for embedded files in the image
```
binwalk chall.png
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 264 x 191, 8-bit colormap, non-interlaced
48            0x30            PNG image, 1200 x 1200, 8-bit/color RGBA, non-interlaced
89            0x59            Zlib compressed data, default compression
```
I found this interresting second image (the 1200*1200 one) in the file. So i extreacted it : 
```
binwalk -D=".*" chall.png
```
And when i looked at the image, the flag was their : shakictf{Y0u_4R3_aM4z1nG!!!!}
