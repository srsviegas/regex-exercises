# Check if at is present in the given byte input data

import re

ip = b"tiger imp goat"
print(bool(re.search(b"at", ip)))
