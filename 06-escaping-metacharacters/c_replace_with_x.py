"""Replace any matching element from the list items with X for given the input strings.
Match the elements from items literally. Assume no two elements of items will result in
any matching conflict."""

import re

items = ["a.b", "3+n", r"x\y\z", "qty||price", "{n}"]
pat = re.compile("|".join(re.escape(e) for e in items))

print(pat.sub("X", "0a.bcd"))
print(pat.sub("X", "E{n}AMPLE"))
print(pat.sub("X", r"43+n2 ax\y\ze"))
