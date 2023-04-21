# For the given input list, replace hand with X for all elements that start with hand
# followed by at least one word character

import re

items = ["handed", "hand", "handy", "un-handed", "handle", "hand-2"]
sub = [re.sub(r"^hand\B", "X", e) for e in items]

print(sub)
