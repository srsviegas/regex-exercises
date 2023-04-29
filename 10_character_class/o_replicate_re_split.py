"""
By default, the str.split() method will split on whitespace and remove empty strings from
the result. Which re module function would you use to replicate this functionality?

Answer: re.findall() can be used to achieve the same results.
"""

from colorama import Fore, Style
import re

ip = " \t\r  so  pole\t\t\t\n\nlit in to \r\n\v\f  "

print(Fore.LIGHTBLUE_EX + "str.split()" + Style.RESET_ALL)
print(ip.split())

print(Fore.LIGHTMAGENTA_EX + "re.findall()" + Style.RESET_ALL)
print(re.findall(r"\w+", ip))
