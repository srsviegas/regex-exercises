# Replace all occurrences of \e with e

import re

ip = r"th\er\e ar\e common asp\ects among th\e alt\ernations"
sub = re.sub("\\\e", "e", ip)

print(sub)
