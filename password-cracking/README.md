# Password Cracking
* [hashcat](hashcat) - Hashcat notes and rules
* [john](john) - John the Ripper notes
* [sanitize.py](sanitize.py) - Sanitize wordlists

# Wordlists
* [clem9669](https://github.com/clem9669/wordlists) - A collection of wordlists


### sanitize.py
```
python3 -m pip install num2words word2number
python3 sanitize.py
python3 sanitize.py [-h] -w WORDLIST [-n NUMBERS] [-c CHARS] [-p PHRASES]
python3 sanitize.py -w rockyou.txt -c '!@#$%^&*()' -p '2000'
```

-c - Will strip specific characters
-p - Will remove specific phrases (comma separated)
