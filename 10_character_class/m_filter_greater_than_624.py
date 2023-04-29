# For the given list, filter all elements containing any number sequence greater than 624

import re

items = ["hi0000432abcd", "car00625", "42_624 0512", "3.14 96 2 foo1234baz"]
filtered = [e for e in items if any(int(m[0]) > 624 for m in re.finditer(r"\d+", e))]

print(filtered)
