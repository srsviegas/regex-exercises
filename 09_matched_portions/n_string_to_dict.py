# Convert the comma separated strings to corresponding dict objects as shown below

import re

row1 = "name:rohan,maths:75,phy:89,"
# Expected: {'name': 'rohan', 'maths': '75', 'phy': '89'}
row2 = "name:rose,maths:88,phy:92,"
# Expected: {'name': 'rose', 'maths': '88', 'phy': '92'}

pat = re.compile(r"(.+?):(.+?),")
dict1 = {m[1]: m[2] for m in pat.finditer(row1)}
dict2 = {m[1]: m[2] for m in pat.finditer(row1)}

print(dict1)
print(dict2)
