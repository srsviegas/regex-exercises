"""For the given input string, replace all occurrences of digit sequences with only the
unique non-repeating sequence. For example, 232323 should be changed to 23 and 897897
should be changed to 897. If there are no repeats (for example 1234) or if the repeats
end prematurely (for example 12121), it should not be changed"""

import re

ip = "1234 2323 453545354535 9339 11 60260260"
op = re.sub(r"\b(\d+)\1+\b", r"\1", ip)

print(op)
