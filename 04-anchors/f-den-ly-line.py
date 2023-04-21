# For the given list, filter all elements having a line starting with den or ending with ly

import re

items = ["lovely", "1\ndentist", "2 lonely", "eden", "fly\nfar", "dent"]
filtered = [
    e
    for e in items
    if re.search(r"^den", e, flags=re.M) or re.search(r"ly$", e, flags=re.M)
]

print(filtered)
