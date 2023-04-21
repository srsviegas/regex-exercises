# Check if the given strings start with "be"

import re

lines = ["be nice", '"best!"', "better?", "oh no\nbear spotted"]
pat = re.compile(r"\Abe")

for line in lines:
    print(bool(pat.search(line)))
