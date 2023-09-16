payload = "__import__('os').system('ls')"

for c in payload:
    hex_c = hex(ord(c))[2:]
    hex_c = "\\x" + hex_c
    print(hex_c, end="")
