# For the list words, filter all elements not containing 'u' or 'w' or 'ee' or '-'

import re

words = ["p-t", "you", "tea", "heel", "owe", "new", "reed", "ear"]
filtered = [w for w in words if not re.search(r"[uw-]|ee", w)]

print(filtered)
