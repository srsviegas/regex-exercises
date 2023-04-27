# Use re.split() to get the output as shown below for given input strings

import re

s1 = 'go there  //   "this // that"'  # ['go there', '"this // that"']
s2 = "a//b // c//d e//f // 4//5"  # ['a//b', 'c//d e//f // 4//5']
s3 = "42// hi//bye//see // carefully"  # ['42// hi//bye//see', 'carefully']

pat = re.compile(r" +// +")

print(pat.split(s1, maxsplit=1))
print(pat.split(s2, maxsplit=1))
print(pat.split(s3, maxsplit=1))
