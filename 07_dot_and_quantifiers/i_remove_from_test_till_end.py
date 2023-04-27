"""For the given input strings, remove everything from the first occurrence of 'test'
(irrespective of case) till the end of the string, provided 'test' isn't at the end of
the string"""

import re

s1 = "this is a Test"
s2 = "always test your RE for corner cases"
s3 = "a TEST of skill tests?"

pat = re.compile(r"test.+", re.I)

print(pat.sub("", s1))
print(pat.sub("", s2))
print(pat.sub("", s3))
