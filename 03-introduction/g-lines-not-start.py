# For the given input string, display all lines not containing start irrespective of case

import re

para = """good start
Start working on that
project you always wanted
stars are shining brightly
hi there
start and try to
finish the book
bye"""

pat = re.compile(r"start", flags=re.IGNORECASE)

for line in para.splitlines():
    if not pat.search(line):
        print(line)
