"""Find the starting index of the first occurrence of 'is' or 'the' or 'was' or 'to' for
the given input strings"""

import re

s1 = "match after the last newline character"
s2 = "and then you want to test"
s3 = "this is good bye then"
s4 = "who was there to see?"

pat = re.compile(r"is|the|was|to")

print(pat.search(s1).start())
print(pat.search(s2).start())
print(pat.search(s3).start())
print(pat.search(s4).start())
