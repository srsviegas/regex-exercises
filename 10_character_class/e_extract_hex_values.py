"""Extract all hex character sequences, with '0x' optional prefix. Match the characters
case insensitively, and the sequences shouldn't be surrounded by other word characters"""

import re

str1 = "128A foo 0xfe32 34 0xbar"
str2 = "0XDEADBEEF place 0x0ff1ce bad"

hex_seq = re.compile(r"\b(0x)?[\da-f]+\b", flags=re.IGNORECASE)

print([m[0] for m in hex_seq.finditer(str1)])
print([m[0] for m in hex_seq.finditer(str2)])
