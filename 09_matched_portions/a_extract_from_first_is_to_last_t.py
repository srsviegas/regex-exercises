# For the given strings, extract the matching portion from the first 'is' to the last 't'

import re

str1 = "This the biggest fruit you have seen?"
str2 = "Your mission is to read and practice consistently"

pat = re.compile(r"is(.*)t")

print(pat.search(str1).group())
print(pat.search(str2).group())
