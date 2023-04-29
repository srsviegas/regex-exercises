"""The given input strings contain fields separated by , and fields can be empty too.
Replace last three fields with WHTSZ323"""

import re

row1 = "(2),kite,12,,D,C,,"
row2 = "hi,bye,sun,moon"

pat = re.compile(r"(,[^,]*){3}$")

print(pat.sub(",WHTSZ323", row1))
print(pat.sub(",WHTSZ323", row2))
