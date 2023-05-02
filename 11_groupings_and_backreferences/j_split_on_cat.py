# Split the given input string on one or more repeated sequence of cat

import re

ip = "firecatlioncatcatcatbearcatcatparrot"
split = re.split(r"(?:cat)+", ip)

print(split)
