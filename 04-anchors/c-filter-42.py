# For the given input list, filter all elements that contain 42 surrounded by word characters

import re

words = ["hi42bye", "nice1423", "bad42", "cool_42a", "42fake", "_42_"]
filtered = [w for w in words if re.search(r"\B42\B", w)]

print(filtered)
