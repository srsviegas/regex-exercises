"""This is an extension to the previous question.
* For row1, find the sum of integers of each tuple element. For example, sum of -2 and 5
is 3.
* For row2, find the sum of floating-point numbers of each tuple element. For example,
sum of 1.32 and -3.14 is -1.82."""

import re

row1 = "-2,5 4,+3 +42,-53 4356246,-357532354 "
row2 = "1.32,-3.14 634,5.63 63.3e3,9907809345343.235 "

pat = re.compile(r"(.+?),(.+?) ")

print([int(a) + int(b) for a, b in pat.findall(row1)])
print([float(a) + float(b) for a, b in pat.findall(row2)])
