"""Filter all whole elements with optional whitespaces at the start followed by three to
five non-digit characters. Whitespaces at the start should not be part of the calculation
for non-digit characters"""

import re

items = ["\t \ncat", "goal", " oh", "he-he", "goal2", "ok ", "sparrow"]
filtered = [e for e in items if re.fullmatch(r"\s*+\D{3,5}", e)]

print(filtered)
