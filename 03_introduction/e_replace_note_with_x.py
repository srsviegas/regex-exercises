# Replace all occurrences of note irrespective of case with X

import re

ip = "This note should not be NoTeD"
print(re.sub(r"note", "X", ip, flags=re.IGNORECASE))
