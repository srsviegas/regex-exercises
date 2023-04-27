# Use re.split() to get the output as shown for the given input strings.

import re

eqn1 = "a+42//5-c"  # ['a+', '-c']
eqn2 = "pressure*3+42/5-14256"  # ['pressure*3+', '-14256']
eqn3 = "r*42-5/3+42///5-42/53+a"  # ['r*42-5/3+42///5-', '3+a']

pat = re.compile(r"42//?5")

print(pat.split(eqn1))
print(pat.split(eqn2))
print(pat.split(eqn3))
