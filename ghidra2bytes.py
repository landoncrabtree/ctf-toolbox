import binascii
import argparse

parser = argparse.ArgumentParser(description="Convert Ghidra output to bytes")
parser.add_argument("-i", "--input", help="Ghidra decompilation output", required=True)
parser.add_argument("-o", "--output", help="File to output to", required=True)
args = parser.parse_args()

ghidra_file = ""
with open(args.input, "r") as f:
    ghidra_file = f.read()

# unhexlify the bytes and return an array
def convert_ghidra(ghidra: str):
  return_array = []
  for line in ghidra.split("\n"):
    line = line.strip()
    if line == "": continue
    line = line.split(" = ")[1].split(";")[0]
    if line[0] == "-": 
        line = line[1:] # remove the negative sign
        decimal = int(line, 16) # convert hex -> decimal
        line = hex(256-decimal) # convert decimal -> hex
    line = line.replace("0x", "") # remove the 0x
    if len(line) % 2 != 0: line = "0" + line # add a 0 if the length is odd
    return_array.append(binascii.unhexlify(line)) # unhexlify the bytes
  return return_array

# Do operations (like XOR)
xor_key = 0xaa
for value in convert_ghidra(ghidra_file):
    decimal_value = int.from_bytes(value, byteorder="little")
    print(chr(decimal_value ^ xor_key), end="")

# Write bytes to file
with open(args.output, "wb") as f:
    for value in convert_ghidra(ghidra_file):
        f.write(value)
