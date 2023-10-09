# John the Ripper

## Wordlist Attack
```bash
john --format=md5 --wordlist=rockyou.txt hash.txt
```

* --format=md5 - Hash type (md5)
* --wordlist=rockyou.txt - Wordlist
* hash.txt - File containing hash(es)

## Wordlist Attack + Rules
```bash
john --format=md5 --wordlist=rockyou.txt --rules=best64.rule hash.txt
```

* --format=md5 - Hash type (md5)
* --wordlist=rockyou.txt - Wordlist
* --rules=best64.rule - Rules file
* hash.txt - File containing hash(es)

## Bruteforce Attack
```bash
john --format=md5 --incremental=alnum hash.txt
```

* --format=md5 - Hash type (md5)
* --incremental=alnum - Character set
* hash.txt - File containing hash(es)

## Bruteforce Attack + Rules
```bash
john --format=md5 --incremental=alnum --rules=best64.rule hash.txt
```

* --format=md5 - Hash type (md5)
* --incremental=alnum - Character set
* --rules=best64.rule - Rules file
* hash.txt - File containing hash(es)

## Hybrid Attack (Wordlist + Mask)
```bash
john --format=md5 --mask='?d?d?d?d' hash.txt --wordlist=rockyou.txt
```

* --format=md5 - Hash type (md5)
* --mask='?d?d?d?d' - Character set
* hash.txt - File containing hash(es)
* --wordlist=rockyou.txt - Wordlist


## Hybrid Attack (Mask + Wordlist)
```bash
john --format=md5 --mask='?d?d?d?d' --wordlist=rockyou.txt hash.txt
```

* --format=md5 - Hash type (md5)
* --mask='?d?d?d?d' - Character set
* --wordlist=rockyou.txt - Wordlist
* hash.txt - File containing hash(es)

## Character Sets
* ?l - abcdefghijklmnopqrstuvwxyz
* ?u - ABCDEFGHIJKLMNOPQRSTUVWXYZ
* ?d - 0123456789
* ?s -  !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
* ?a - ?l?u?d?s
* ?b - 0x00 - 0xff



