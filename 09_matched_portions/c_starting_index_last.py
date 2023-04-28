"""Find the starting index of the last occurrence of 'is' or 'the' or 'was' or 'to' for
the given input strings"""

import re

s1 = "match after the last newline character"
s2 = "and then you want to test"
s3 = "this is good bye then"
s4 = "who was there to see?"

pat = re.compile(r"is|the|was|to")

print(list(pat.finditer(s1))[-1].start())
print(list(pat.finditer(s2))[-1].start())
print(list(pat.finditer(s3))[-1].start())
print(list(pat.finditer(s4))[-1].start())
