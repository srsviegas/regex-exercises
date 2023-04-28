"""Use re.split() to get the output as shown below"""

import re

ip = "42:no-output;1000:car-tr:u-ck;SQEX49801"
# Expected: ['42', 'output', '1000', 'tr:u-ck', 'SQEX49801']

split = re.split(r":.{2,}?-|;", ip)

print(split)
