# Modify the given regular expression such that it gives the expected result

from colorama import Fore, Style
import re

ip = "( S:12 E:5 S:4 and E:123 ok S:100 & E:10 S:1 - E:2 S:42 E:43 )"

# wrong output
# ['S:12 E:5 S:4 and E:123', 'S:100 & E:10', 'S:1 - E:2 S:42 E:43']
print(
    Fore.LIGHTRED_EX + "wrong:" + Style.RESET_ALL, re.findall(r"S:\d+.*?E:\d{2,}", ip)
)

# expected output
# ['S:4 and E:123', 'S:100 & E:10', 'S:42 E:43']
print(
    Fore.LIGHTGREEN_EX + "wrong:" + Style.RESET_ALL,
    re.findall(r"(?>S:\d+.*?E:)\d{2,}", ip),
)
