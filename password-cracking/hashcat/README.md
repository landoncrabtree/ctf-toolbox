# Hashcat

## Rules
* [OneRuleToRuleThemAllStill.rule](https://github.com/stealthsploit/OneRuleToRuleThemStill) -  A revamped and updated version of my original OneRuleToRuleThemAll hashcat rule 
* [clem9669](https://github.com/clem9669/hashcat-rule) - A collection of hashcat rules

## Wordlist Attack
```bash
hashcat -m 0 -a 0 hash.txt rockyou.txt
```

* -m 0 - Hash type (0 = MD5)
* -a 0 - Attack mode (0 = Straight)
* hash.txt - File containing hash(es)
* rockyou.txt - Wordlist

## Wordlist Attack + Rules
```bash
hashcat -m 0 -a 0 hash.txt rockyou.txt -r best64.rule
```

* -m 0 - Hash type (0 = MD5)
* -a 0 - Attack mode (0 = Straight)
* hash.txt - File containing hash(es)
* rockyou.txt - Wordlist
* -r best64.rule - Rules file

## Bruteforce Attack
```bash
hashcat -m 0 -a 3 hash.txt ?a?a?a?a?a?a?a?a
```

* -m 0 - Hash type (0 = MD5)
* -a 3 - Attack mode (3 = Brute-force)
* hash.txt - File containing hash(es)
* ?a?a?a?a?a?a?a?a - Character set

## Bruteforce Attack + Rules
```bash
hashcat -m 0 -a 3 hash.txt ?a?a?a?a?a?a?a?a -r best64.rule
```

* -m 0 - Hash type (0 = MD5)
* -a 3 - Attack mode (3 = Brute-force)
* hash.txt - File containing hash(es)
* ?a?a?a?a?a?a?a?a - Character set
* -r best64.rule - Rules file

## Hybrid Attack (Wordlist + Mask)
```bash
hashcat -m 0 -a 6 hash.txt rockyou.txt ?d?d?d?d
```

* -m 0 - Hash type (0 = MD5)
* -a 6 - Attack mode (6 = Wordlist + Mask)
* hash.txt - File containing hash(es)
* ?d?d?d?d - Character set

## Hybrid Attack (Mask + Wordlist)
```bash
hashcat -m 0 -a 7 hash.txt ?d?d?d?d rockyou.txt
```

* -m 0 - Hash type (0 = MD5)
* -a 7 - Attack mode (7 = Mask + Wordlist)
* hash.txt - File containing hash(es)
* ?d?d?d?d - Character set

## Combine Wordlists
The password is an animal followed by a color.

animal.dic
```
dog
cat
bird
```

color.dic
```
red
blue
green
```

```bash
hashcat -m 0 -a 1 hash.txt animal.dic color.dic
```

* -m 0 - Hash type (0 = MD5)
* -a 1 - Attack mode (1 = Combinator Attack)
* hash.txt - File containing hash(es)
* animal.dic - Wordlist 1
* color.dic - Wordlist 2
* ... - Wordlist n

## Character Sets
* ?l - abcdefghijklmnopqrstuvwxyz
* ?u - ABCDEFGHIJKLMNOPQRSTUVWXYZ
* ?d - 0123456789
* ?s - !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
* ?a - ?l?u?d?s
* ?b - 0x00 - 0xff



