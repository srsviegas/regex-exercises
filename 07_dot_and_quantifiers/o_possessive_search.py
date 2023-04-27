# Modify the given regular expression such that it gives the expected results

from colorama import Fore, Style
import re

s1 = "appleabcabcabcapricot"
s2 = "bananabcabcabcdelicious"

# wrong output
pat = re.compile(r"(abc)+a")
print(Fore.LIGHTRED_EX + "(-) Wrong:" + Style.RESET_ALL)
print(bool(pat.search(s1)))  # True
print(bool(pat.search(s2)))  # True

# expected output
pat = re.compile(r"(abc)++a")
print(Fore.LIGHTGREEN_EX + "(+) Correct:" + Style.RESET_ALL)
print(bool(pat.search(s1)))  # True
print(bool(pat.search(s2)))  # False
