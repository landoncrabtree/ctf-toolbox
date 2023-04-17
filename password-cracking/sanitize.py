# sanitize.py
# sanitize wordlists

import argparse
from num2words import num2words
from word2number import w2n
import re

def convert_to_word_form(s):
    pattern = re.compile(r'\d+|\D+')
    new_s = ''
    for match in pattern.finditer(s):
        group = match.group()
        if group.isdigit():
            new_s += num2words(int(group), lang='en')
        else:
            new_s += group
    return new_s.replace(' ', '')

# WIP
def convert_to_number_form(s):
    tmp = ''
    num = 0
    for c in s:
        tmp += c
        try:
            w2n.word_to_num(tmp)
            num = w2n.word_to_num(tmp)
            s = s.replace(tmp, str(num))
        except:
            if num != 0:
                tmp = ''
                continue
            continue
    return s
    

parser = argparse.ArgumentParser()
parser.add_argument('-w', '--wordlist', help='wordlist to cleanse', required=True)
parser.add_argument('-n', '--numbers', help='number replacement mode', required=False, type=int)

# -c @!#%$^&*()_+|}{:?><~`-=[]\;',./
parser.add_argument('-c', '--chars', help='symbols to replace', required=False, type=str)

# -p http,xml,html,php,asp,aspx,js,css,sql,etc
parser.add_argument('-p', '--phrases', help='phrases to replace', required=False, type=str)
args = parser.parse_args()

if args.numbers:
    number = int(args.numbers)
    if number not in [1, 2]:
        print("Invalid number mode.")
        print("1 - Replace english with the number representation. ie; 'fifty' -> 50")
        print("1 - Replace number with the english representation. ie; 50 -> 'fifty'")

new = open(f"{args.wordlist}-cleansed.txt", 'w')

with open(args.wordlist, 'r') as f:
    for line in f:
        line = line.strip().lower().replace(' ', '')
        if args.numbers:
            # int -> english (50 -> fifty)
            if number==1:
                line = convert_to_word_form(line)
            # english -> int (fifty -> 50)
            elif number==2:
                line = convert_to_number_form(line)
        if args.chars:
            for c in args.chars:
                line = line.replace(c, '')
        if args.phrases:
            if (len(args.phrases.split(', ')) > 0):
                for phrase in args.phrases.split(', '):
                    line = line.replace(phrase, '')
            else:
                for phrase in args.phrases.split(','):
                    line = line.replace(phrase, '')
        new.write(f"{line}\n")
