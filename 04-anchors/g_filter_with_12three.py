# For the given input list, filter all whole elements "12\nthree" irrespective of case

import re

items = ["12\nthree\n", "12\nThree", "12\nthree\n4", "12\nthree"]
filtered = [e for e in items if re.search(r"\A12\nthree\Z", e, flags=re.I)]

print(filtered)
