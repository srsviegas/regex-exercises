"""Replace all whole words with X that start and end with the same word character
(irrespective of case). Single character word should get replaced with X too, as it
satisfies the stated condition"""

import re

ip = "oreo not a _a2_ Roar took 22"
sub = re.sub(r"\b(?:\w|(\w)\w*\1)\b", "X", ip, flags=re.I)

print(sub)
