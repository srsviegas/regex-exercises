# For the given input string, change whole word mall to 1234 only if it is at the start of a line.

import re

para = """\
(mall) call ball pall
ball fall wall tall
mall call ball pall
wall mall ball fall
mallet wallet malls
mall:call:ball:pall"""

sub = re.sub(r"^mall\b", "1234", para, flags=re.MULTILINE)

print(sub)
