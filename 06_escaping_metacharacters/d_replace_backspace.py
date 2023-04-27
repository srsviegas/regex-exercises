# Replace the backspace character \b with a single space character for the given input string.

import re

ip = "123\b456"
sub = re.sub("\\\b", " ", ip)

print(sub)
