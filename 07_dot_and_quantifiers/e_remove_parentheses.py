# For the given strings, construct a RE to get the output as shown below

import re

str1 = "a+b(addition)"  # 'a+b'
str2 = "a/b(division) + c%d(#modulo)"  # 'a/b + c%d'
str3 = "Hi there(greeting). Nice day(a(b)"  # 'Hi there. Nice day'

remove_parentheses = re.compile(r"\(.*?\)")

print(remove_parentheses.sub("", str1))
print(remove_parentheses.sub("", str2))
print(remove_parentheses.sub("", str3))
