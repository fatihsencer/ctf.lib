Verilen zip'in hash'ini zip2john ile cikartiyoru

```bash

zip2john strong_password.zip > hash

```

bu hash'i rockyou ile crackledigimiz zaman sifreyi buluyorduk.

```bash

john hash --wordlists=/usr/share/wordlists/rockyou.txt

```


sifreyi bulduktan sonra zipin icindekileri cikartip flag'i buluyoruz.
