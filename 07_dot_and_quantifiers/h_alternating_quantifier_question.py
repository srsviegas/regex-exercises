"""
(a*|b*) is same as (a|b)* — True or False?

Answer: False
(a*|b*) will match everything after the first a or b
(a|b)* will match any sequence of a's and b's
"""

from colorama import Fore, Style
import re

ex = "plink incoming tint winter in caution sentient"

if re.sub(r"(n*|m*)", "X", ex) == re.sub(r"(n|m)*", "X", ex):
    print(
        Fore.LIGHTGREEN_EX + "(+) '(a*|b*)' is the same as '(a|b)*'" + Style.RESET_ALL
    )
else:
    print(
        Fore.LIGHTRED_EX + "(-) '(a*|b*)' is not the same as '(a|b)*'" + Style.RESET_ALL
    )
