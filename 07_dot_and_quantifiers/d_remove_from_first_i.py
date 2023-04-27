"""For the given input strings, remove everything from the first occurrence of 'i' till the
end of the string"""

import re

s1 = "remove the special meaning of such constructs"
s2 = "characters while constructing"
s3 = "input output"

pat = re.compile(r"i.*")

print(pat.sub("", s1))
print(pat.sub("", s2))
print(pat.sub("", s3))
