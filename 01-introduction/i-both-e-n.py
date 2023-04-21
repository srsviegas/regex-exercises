# For the given list, filter all elements that contain both e and n

import re

items = ["goal", "new", "user", "sit", "eat", "dinner"]
print([w for w in items if re.search(r"e", w) and re.search(r"n", w)])
