"""For the list items, filter all elements starting with hand and ending immediately with
s or y or le"""

import re

items = ["-handy", "hand", "handy", "unhand", "hands", "hand-icy", "handle"]
filtered = [e for e in items if re.match(r"hand([sy]|le)", e)]

print(filtered)
