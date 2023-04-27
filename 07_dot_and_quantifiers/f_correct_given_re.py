# Correct the given RE to get the expected output

from colorama import Fore, Style
import re

words = "plink incoming tint winter in caution sentient"

# wrong output -> 'plXk XcomXg tX wXer X cautX sentient'
change = re.compile(r"int|in|ion|ing|inco|inter|ink")
print(Fore.LIGHTRED_EX + "(-) Wrong:" + Style.RESET_ALL, change.sub("X", words))

# expected output -> 'plX XmX tX wX X cautX sentient'
change = re.compile(r"i(on|n(t(er)?|g|co|k)?)")
print(Fore.LIGHTGREEN_EX + "(+) Correct:" + Style.RESET_ALL, change.sub("X", words))
