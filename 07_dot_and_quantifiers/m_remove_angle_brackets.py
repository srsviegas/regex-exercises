"""
Can you reason out why this code results in the output shown? The aim was to remove all
<characters> patterns but not the <> ones. The expected result was 'a 1<> b 2<> c'.

>>> ip = 'a<apple> 1<> b<bye> 2<> c<cat>'

>>> re.sub(r'<.+?>', '', ip)
'a 1 2'

Answer: For the example shown above, the engine will consider '> b<bye' as a match for the
expression '.+?'. Therefore, the character '>' should be excluded from the pattern to get
the expected result.
"""

import re

ip = "a<apple> 1<> b<bye> 2<> c<cat>"
sub = re.sub(r"<[^>.]+?>", "", ip)

print(sub)
