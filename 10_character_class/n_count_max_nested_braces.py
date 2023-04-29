"""Count the maximum depth of nested braces for the given strings. Unbalanced or wrongly
ordered braces should return -1. Note that this will require a mix of regular expressions
and Python code"""

import re


def max_nested_braces(string):
    """Counts the maximum depth of nested braces for the given string"""
    count = 0
    while re.search(r"{.*}", string, flags=re.DOTALL):
        string = re.sub(r"{([^{}]*)}", lambda m: m[1], string)
        count += 1
    if re.search(r"[{}]", string):
        return -1
    return count


print(max_nested_braces("a*b"))  # Expected: 0
print(max_nested_braces("}a+b{"))  # Expected: -1
print(max_nested_braces("a*b+{}"))  # Expected: 1
print(max_nested_braces("{{a+2}*{b+c}+e}"))  # Expected: 2
print(max_nested_braces("{{a+2}*{b+{c*d}}+e}"))  # Expected: 3
print(max_nested_braces("{{a+2}*{\n{b+{c*d}}+e*d}}"))  # Expected: 4
print(max_nested_braces("a*{b+c*{e*3.14}}}"))  # Expected: -1
