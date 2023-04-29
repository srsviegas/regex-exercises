"""Delete all occurrences of the sequence <characters> where characters is one or more
non '>' characters and cannot be empty"""

import re

ip = "a<ap\nple> 1<> b<bye> 2<> c<cat>"
deleted = re.sub(r"<[^>]+>", "", ip)

print(deleted)
