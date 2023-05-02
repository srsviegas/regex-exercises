"""Convert the comma separated strings to corresponding dict objects as shown below. The
keys are name, maths and phy for the three fields in the input strings"""

import re

row1 = "rohan,75,89"
row2 = "rose,88,92"

pat = re.compile(r"(?P<name>\w+),(?P<maths>\d+),(?P<phy>\d+)")

print(pat.search(row1).groupdict())
print(pat.search(row2).groupdict())
