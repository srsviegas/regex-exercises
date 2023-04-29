# Convert the given input string to two different lists as shown below

import re

ip = "price_42 roast^\t\n^-ice==cat\neast"

list1 = re.findall(r"\w+", ip)
list2 = re.findall(r"\w+|\W+", ip)

print(list1)
# Expected: ['price_42', 'roast', 'ice', 'cat', 'east']
print(list2)
# Expected: ['price_42', ' ', 'roast', '^\t\n^-', 'ice', '==', 'cat', '\n', 'east']
