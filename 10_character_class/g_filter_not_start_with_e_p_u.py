# For the list words, filter all elements not starting with 'e' or 'p' or 'u'

import re

words = ["surrender", "unicorn", "newer", "door", "empty", "eel", "(pest)"]
filtered = [w for w in words if re.match(r"[^epu].*", w)]

print(filtered)
