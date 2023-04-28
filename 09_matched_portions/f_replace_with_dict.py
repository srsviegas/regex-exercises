"""Replace all occurrences of 'par' with 'spar', 'spare' with 'extra' and 'park' with
'garden' for the given input strings"""

import re

str1 = "apartment has a park"
str2 = "do you have a spare cable"
str3 = "write a parser"

replacements = {"par": "spar", "spare": "extra", "park": "garden"}
pat = re.compile("|".join(sorted(replacements.keys(), key=len, reverse=True)))
replace_match = lambda m: replacements[m[0]]

print(pat.sub(replace_match, str1))
print(pat.sub(replace_match, str2))
print(pat.sub(replace_match, str3))
