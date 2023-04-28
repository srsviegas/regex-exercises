"""Extract all words between '(' and ')' from the given input string as a list. Assume
that the input will not contain any broken parentheses"""

import re

ip = "another (way) to reuse (portion) matched (by) capture groups"
extracted = re.findall(r"\((.*?)\)", ip)

print(extracted)
