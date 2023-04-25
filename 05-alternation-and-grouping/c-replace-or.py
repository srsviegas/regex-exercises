# For the given strings, replace all occurrences of removed or reed or received or refused with X

import re

s1 = "creed refuse removed read"
s2 = "refused reed redo received"
pat = re.compile(r"removed|reed|received|refused")

print(pat.sub("X", s1))
print(pat.sub("X", s2))
