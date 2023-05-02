"""The given input string has sequences made up of words separated by : or . and such
sequences will end when : or . is not followed by a word character. For all such
sequences, display only the last word followed by - followed by the first word."""

import re

ip = "wow:Good:2_two.five: hi-2 bye kite.777:water."
it = re.finditer(r"(?P<first>\w+)[:.](?:(?P<last>\w+)[:.])+", ip)

print([m.expand(r"\g<last>-\g<first>") for m in it])
