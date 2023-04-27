"""For the input list words, filter all elements starting with s and containing e and t
in any order"""

import re

words = ["sequoia", "subtle", "exhibit", "a set", "sets", "tests", "site"]
filtered = [w for w in words if re.search(r"^s.*(e.*t|t.*e)", w)]

print(filtered)
