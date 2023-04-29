"""Delete from '(' to the next occurrence of ')' unless they contain parentheses characters
in between"""

import re

str1 = "def factorial()"
str2 = "a/b(division) + c%d(#modulo) - (e+(j/k-3)*4)"
str3 = "Hi there(greeting). Nice day(a(b)"

remove_parentheses = re.compile(r"\([^)(]*\)")

print(remove_parentheses.sub("", str1))
print(remove_parentheses.sub("", str2))
print(remove_parentheses.sub("", str3))
