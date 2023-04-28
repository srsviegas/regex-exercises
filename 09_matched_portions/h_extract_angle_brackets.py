"""Extract all occurrences of '<' up to the next occurrence of '>', provided there is at
least one character in between '<' and '>'"""

import re

ip = "a<apple> 1<> b<bye> 2<> c<cat>"
extracted = re.findall(r"<.+?>", ip)

print(extracted)
