# PicoCTF2021 | Transformation

By [fatihsencer](https://github.com/fatihsencer)

## Açıklama
I wonder what this really is... enc ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

## Analiz
Şifrelenmiş bir adet dosyamız var. Açıklamaya baktığımızda nasıl şifrelendiğini görebiliriz. İlk indeximizin ascii değeri bitsel işleme sokulmuş ( << 2^8 ). Ardından bu değere sonraki index'in ascii değeri eklenmiş. Bu işlem her 2 adımda bir tekrarlanmış.

## Çözüm
Öncelikle bize verilen dosyanın içindeki karakterlerin ascii değerini aldım. 

```
crypted = [28777, 25455, 17236, 18043, 12598, 24418, 26996, 29535, 26990, 29556, 13108, 25695, 28518, 24376, 24368, SECRET, SECRET, SECRET, SECRET]
```

Bulduğum ascii değerlere yapılan işlemlerin tersini yaptım. ( >> 2^8 ) 

```
for x in range(0,len(crypted)):

    print(chr(int(crypted[x]/(2**8))),end='')
    
-> pcCF1_isis3do__SECRET
```

Kısmen şireyi buldum fakat eksik olan harfler vardı. Bunun sebebi adımların 2şer 2şer yapılıp 2. indexin 1. index'e eklenmesi.

Eklenen değerleri, bulduğumuz harfi tekrar bitsel işleme sokup, ilk başta şifreli dosyanın içerisinden elde ettiğimiz ascii değerlerinden çıkartıp  eklenen harfin ascii değerini buldum.

p üzerinden örnek vericek olursak 

```
ord('p')*(2**8) = 28672

crypted[0] = 28777

28777 - 28672 = 105 

chr(105) = i

```

Bunu bütün değerlere uyguladığımda bayrağı buldum.

*Flag: picoCTF{16_bits_inst34d_of_8_SECRET}*
