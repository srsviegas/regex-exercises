"""For the given list of strings, change the elements into a tuple of original element and
the number of times 't' occurs in that element"""

import re

words = ["sequoia", "attest", "tattletale", "asset"]
processed = [re.subn(r"t", "t", w) for w in words]

print(processed)
