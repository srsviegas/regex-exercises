"""Replace any matching item from the list eqns with X for given the string ip. Match the
items from eqns literally."""

import re

ip = "3-(a^b)+2*(a^b)-(a/b)+3"
eqns = ["(a^b)", "(a/b)", "(a^b)+2"]
pat = re.compile("|".join(re.escape(e) for e in sorted(eqns, key=len, reverse=True)))

print(pat.sub("X", ip))
