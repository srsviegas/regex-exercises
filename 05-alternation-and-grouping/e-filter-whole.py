# Filter all whole elements from the input list items based on elements listed in words

import re

items = ["slate", "later", "plate", "late", "slates", "slated "]
words = ["late", "later", "slated"]
pat = re.compile(f"\A{'|'.join(words)}\Z")
filtered = [e for e in items if pat.search(e)]

print(filtered)
