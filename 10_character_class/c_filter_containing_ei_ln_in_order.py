"""For the list words, filter all elements containing 'e' or 'i' followed by 'l' or 'n'. Note
that the order mentioned should be followed"""

import re

words = ["surrender", "unicorn", "newer", "door", "empty", "eel", "pest"]
filtered = [w for w in words if re.search(r"[ei].*[ln]", w)]

print(filtered)
