# Replace 42//5 or 42/5 with 8 for the given input

import re

ip = "a+42//5-c pressure*3+42/5-14256"
sub = re.sub(r"42//?5", "8", ip)

print(sub)
