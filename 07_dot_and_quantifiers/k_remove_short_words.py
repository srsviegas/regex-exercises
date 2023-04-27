# For the input list words, remove all elements having less than 6 characters

import re

words = ["sequoia", "subtle", "exhibit", "asset", "sets", "tests", "site"]
filtered = [w for w in words if re.search(r"^.{6,}$", w)]

print(filtered)
