# Replace all whole words 'reed' or 'read' or 'red' with 'X'

import re

ip = "redo red credible :read: rod reed"
sub = re.sub(r"\bre[ae]?d\b", "X", ip)

print(sub)
