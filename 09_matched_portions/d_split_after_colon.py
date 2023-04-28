"""The given input string contains ':' exactly once. Extract all characters after the ':'
as output"""

import re

ip = "fruits:apple, mango, guava, blueberry"
extracted = re.search(r":(.*)", ip).group(1)

print(extracted)
