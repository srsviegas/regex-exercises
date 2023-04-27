# For the given strings, replace all matches from the list words with A

import re

s1 = "plate full of slate"
s2 = "slated for later, don't be late"
words = ["late", "later", "slated"]
pat = re.compile("|".join(sorted(words, key=len, reverse=True)))

print(pat.sub("A", s1))
print(pat.sub("A", s2))
