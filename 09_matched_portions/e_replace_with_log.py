"""The given input strings contains some text followed by '-' followed by a number. Replace
that number with its log value using 'math.log()'."""

import math
import re

s1 = "first-3.14"
s2 = "next-123"

pat = re.compile(r"-(.*)")
match_to_log = lambda m: "-" + str(math.log(float(m[1])))

print(pat.sub(match_to_log, s1))
print(pat.sub(match_to_log, s2))
