"""Surround all whole words with (). Additionally, if the whole word is imp or ant, delete
them. Can you do it with just a single substitution?"""

import re

ip = "tiger imp goat eagle ant important"
sub = re.sub(r"\b(?:imp|ant|(\w+))\b", r"(\1)", ip)

print(sub)
