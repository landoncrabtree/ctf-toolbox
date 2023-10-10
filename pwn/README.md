# Pwn
* [pwntools.sh](pwntools.sh) - Installation script for pwntools
* [solve.py](solve.py) - A template for solving pwn challenges with pwntools
* [ROPGadget](https://github.com/JonathanSalwan/ROPgadget) - A tool for finding ROP gadgets and generating ROP chains
* [angr](https://github.com/angr/angr) - A tool for analyzing binaries
* [CTF-pwn-tips](https://github.com/Naetw/CTF-pwn-tips/blob/master/README.md) - Collection of common vulnerabilities and exploitation techniques
* [Zeratool](https://github.com/ChrisTheCoolHut/Zeratool) - Automatic exploit generation
* [ptrace.c](ptrace.c) - Bypass PTRACE_TRACEME anti-debugging via LD_PRELOAD

  ### ptrace.c
  ```
  gcc -shared ptrace.c -o ptrace.so
  export LD_PRELOAD=./ptrace.so
  (gdb) set environment LD_PRELOAD=./ptrace.so
  ```

