# Add [] around words starting with s and containing e and t in any order

import re

ip = "sequoia subtle exhibit asset sets2 tests si_te"
sub = re.sub(r"(\bs\w*(e\w*t|t\w*e)\w*\b)", r"[\1]", ip)

print(sub)
