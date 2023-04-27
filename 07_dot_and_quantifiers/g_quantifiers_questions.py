"""For the given greedy quantifiers, what would be the equivalent form using the {m,n}
representation?"""

from colorama import Fore, Style
import re

ex = "plink incoming tint winter in caution sentient"

# ? is same as ...
# Answer: {,1}
if re.sub(r"(in)?", "X", ex) == re.sub(r"(in){,1}", "X", ex):
    print(Fore.LIGHTGREEN_EX + "(+) '?' is the same as '{,1}'" + Style.RESET_ALL)
else:
    print(Fore.LIGHTRED_EX + "(-) '?' is not the same as '{,1}'" + Style.RESET_ALL)

# * is same as ...
# Answer: {,}
if re.sub(r"(in)*", "X", ex) == re.sub(r"(in){,}", "X", ex):
    print(Fore.LIGHTGREEN_EX + "(+) '*' is the same as '{,}'" + Style.RESET_ALL)
else:
    print(Fore.LIGHTRED_EX + "(-) '*' is not the same as '{,}'" + Style.RESET_ALL)

# + is same as ...
# Answer: {1,}
if re.sub(r"(in)+", "X", ex) == re.sub(r"(in){1,}", "X", ex):
    print(Fore.LIGHTGREEN_EX + "(+) '+' is the same as '{1,}'" + Style.RESET_ALL)
else:
    print(Fore.LIGHTRED_EX + "(-) '+' is not the same as '{1,}'" + Style.RESET_ALL)
