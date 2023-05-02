"""Replace the space character that occurs after a word ending with a or r with a newline
character."""

import re

ip = "area not a _a2_ roar took 22"
sub = re.sub(r"(a|r)( )", r"\1\n", ip)

print(sub)
