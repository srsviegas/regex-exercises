# For the given list, filter all elements that start with den or end with ly

import re

items = ["lovely", "1\ndentist", "2 lonely", "eden", "fly\n", "dent"]
filtered = [e for e in items if re.search(r"\Aden|ly\Z", e)]

print(filtered)
