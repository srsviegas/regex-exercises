# For the given list, filter all elements that do not contain e

import re

items = ["goal", "new", "user", "sit", "eat", "dinner"]
print([item for item in items if not re.search(r"e", item)])
