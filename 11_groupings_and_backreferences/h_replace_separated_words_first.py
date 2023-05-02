"""Replace sequences made up of words separated by : or . by the first word of the
sequence. Such sequences will end when : or . is not followed by a word character."""

import re

ip = "wow:Good:2_two.five: hi-2 bye kite.777:water."
sub = re.sub(r"(\w+)[:.]\S*", r"\1", ip)

print(sub)
