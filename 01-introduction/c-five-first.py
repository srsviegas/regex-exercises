# Replace only the first occurrence of 5 with five for the given string

import re

ip = "They ate 5 apples and 5 oranges"
print(re.sub(r"5", "five", ip, count=1))
