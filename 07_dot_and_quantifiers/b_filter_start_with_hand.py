"""For the list items, filter all elements starting with 'hand' and ending immediately with
at most one more character or 'le'"""

import re

items = ["handed", "hand", "handled", "handy", "unhand", "hands", "handle"]
filtered = [e for e in items if re.search(r"\Ahand(.?|le)\Z", e)]

print(filtered)
