# For the list words, filter all elements containing 'e' or 'i' and 'l' or 'n' in any order

import re

words = ["surrender", "unicorn", "newer", "door", "empty", "eel", "pest"]
filtered = [w for w in words if re.search(r"[ei].*[ln]|[ln].*[ei]", w)]

print(filtered)
