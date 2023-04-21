# Check whether the given strings contain 0xB0

import re

line1 = "start address: 0xA0, func1 address: 0xC0"
line2 = "end address: 0xFF, func2 address: 0xB0"

print(bool(re.search(r"0xB0", line1)))
print(bool(re.search(r"0xB0", line2)))
