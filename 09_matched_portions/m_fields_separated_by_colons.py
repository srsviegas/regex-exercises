"""The given input string has fields separated by ':'. Each field contains four uppercase
alphabets followed optionally by two digits. Ignore the last field, which is empty. See
docs.python: Match.groups and use re.finditer() to get the output as shown below. If the
optional digits aren't present, show 'NA' instead of None"""

import re

ip = "TWXA42:JWPA:NTED01:"
fields = map(lambda m: m.groups(default="NA"), re.finditer(r"(.{4})(.{2})?:", ip))

print(list(fields))
