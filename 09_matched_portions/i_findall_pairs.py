"""Use re.findall() to get the output as shown below for the given input strings. Note the
characters used in the input strings carefully"""

import re

row1 = "-2,5 4,+3 +42,-53 4356246,-357532354 "
# Expected: [('-2', '5'), ('4', '+3'), ('+42', '-53'), ('4356246', '-357532354')]

row2 = "1.32,-3.14 634,5.63 63.3e3,9907809345343.235 "
# Expected: [('1.32', '-3.14'), ('634', '5.63'), ('63.3e3', '9907809345343.235')]

pat = re.compile(r"(.+?),(.+?) ")

print(pat.findall(row1))
print(pat.findall(row2))
