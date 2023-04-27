"""For the input list words, filter all elements starting with s or t and having a maximum
of 6 characters"""

import re

words = ["sequoia", "subtle", "exhibit", "asset", "sets", "t set", "site"]
filtered = [w for w in words if re.search(r"^(s|t).{,5}$", w)]

print(filtered)
