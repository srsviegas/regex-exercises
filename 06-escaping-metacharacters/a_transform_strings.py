# Transform the given input strings to the expected output using the same logic on both strings

import re

str1 = "(9-2)*5+qty/3-(9-2)*7"  # Expected: '35+qty/3-(9-2)*7'
str2 = "(qty+4)/2-(9-2)*5+pq/4"  # Expected: '(qty+4)/2-35+pq/4'
expr = re.escape("(9-2)*5")
pat = re.compile(expr)

print(pat.sub("35", str1))
print(pat.sub("35", str2))
