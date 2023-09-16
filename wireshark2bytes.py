import binascii
import argparse

parser = argparse.ArgumentParser(description="Convert Wireshark stream to bytes")
parser.add_argument("-i", "--input", help="Wireshark raw stream", required=True)
parser.add_argument("-o", "--output", help="File to output to", required=True)
args = parser.parse_args()

wireshark_file = ""
with open(args.input, "r") as f:
    wireshark_file = f.read()

# unhexlify the bytes and return an array
def convert_wireshark(wireshark: str):
  return_array = []
  for line in wireshark.split("\n"):
    line = line.strip()
    if len(line) % 2 != 0: line = "0" + line # add a 0 if the length is odd
    return_array.append(binascii.unhexlify(line)) # unhexlify the bytes
  print(return_array)
  return return_array

# Write bytes to file
with open(args.output, "wb") as f:
    for value in convert_wireshark(wireshark_file):
        f.write(value)
