r"""
'\b[a-z](on|no)[a-z]\b' is same as '\b[a-z][on]{2}[a-z]\b'. True or False? Sample input
lines shown below might help to understand the differences, if any.

Answer: False. The expression '[on]{2}' can match the sequences 'oo' and 'nn', which the
expression '(on|no)' can't.
"""

from colorama import Fore, Style
import re

ip = "known\nmood\nknow\npony\ninns"

if (re.sub(r"\b[a-z](on|no)[a-z]\b", "X", ip)) == (
    re.sub(r"\b[a-z][on]{2}[a-z]\b", "X", ip)
):
    print(
        Fore.LIGHTGREEN_EX
        + r"(+) '\b[a-z](on|no)[a-z]\b' is the same as '\b[a-z][on]{2}[a-z]\b'"
        + Style.RESET_ALL
    )
else:
    print(
        Fore.LIGHTRED_EX
        + r"(-) '\b[a-z](on|no)[a-z]\b' is not the same as '\b[a-z][on]{2}[a-z]\b'"
        + Style.RESET_ALL
    )
