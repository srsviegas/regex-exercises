# Split the given strings based on consecutive sequence of digit or whitespace characters

import re

str1 = "lion \t Ink32onion Nice"
str2 = "**1\f2\n3star\t7 77\r**"

pat = re.compile(r"[\s\d]+")

print(pat.split(str1))
print(pat.split(str2))
