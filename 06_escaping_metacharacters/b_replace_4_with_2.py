# Replace (4)\| with 2 only at the start or end of the given input strings

import re

s1 = r"2.3/(4)\|6 foo 5.3-(4)\|"
s2 = r"(4)\|42 - (4)\|3"
s3 = "two - (4)\\|\n"
expr = re.escape("(4)\|")
pat = re.compile(f"\A{expr}|{expr}\Z")

print(pat.sub("2", s1))
print(pat.sub("2", s2))
print(pat.sub("2", s3))
