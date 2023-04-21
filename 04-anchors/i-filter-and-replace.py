# For the given input list, filter all elements starting with h. Additionally, replace e
# with X for these filtered elements

import re

items = ["handed", "hand", "handy", "unhanded", "handle", "hand-2"]
filtered = [re.sub(r"e", "X", e) for e in items if re.search(r"\Ah", e)]

print(filtered)
