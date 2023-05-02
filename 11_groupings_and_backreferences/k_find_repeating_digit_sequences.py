"""For the given input string, find all occurrences of digit sequences with at least one
repeating sequence. For example, 232323 and 897897. If the repeats end prematurely, for
example 12121, it should not be matched."""

import re

ip = "1234 2323 453545354535 9339 11 60260260"
pat = re.compile(r"\b(\d+)\1+\b")

# entire sequences in the output
print([m[0] for m in pat.finditer(ip)])

# only the unique sequence in the output
print(pat.findall(ip))
