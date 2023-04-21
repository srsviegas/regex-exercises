# For the given list, filter all elements that contain either a or w

import re

items = ["goal", "new", "user", "sit", "eat", "dinner"]
print([w for w in items if re.search(r"a", w) or re.search(r"w", w)])
