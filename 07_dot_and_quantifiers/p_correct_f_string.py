# Modify the given regular expression such that it gives the expected result

from colorama import Fore, Style
import re

cast = "dragon-unicorn--centaur---mage----healer"
c = "-"

# wrong output -> 'dragon-unicorn--centaur---mage----healer'
sub = re.sub(rf"{c}{3,}", c, cast)
print(Fore.LIGHTRED_EX + "(-) Wrong:" + Style.RESET_ALL, sub)

# expected output -> 'dragon-unicorn--centaur-mage-healer'
sub = re.sub(rf"{c}{{3,}}", c, cast)
print(Fore.LIGHTGREEN_EX + "(+) Correct:" + Style.RESET_ALL, sub)
