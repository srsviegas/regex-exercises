"""Count the number of whole words that have at least two occurrences of consecutive
repeated alphabets. For example, words like stillness and Committee should be counted but
not words like root or readable or rotational"""

import re

ip = """oppressed abandon accommodation bloodless
carelessness committed apparition innkeeper
occasionally afforded embarrassment foolishness
depended successfully succeeded
possession cleanliness suppress"""

counter = len(re.findall(r"\b(\w*(\w)\2\w*(\w)\3\w*)\b", ip))

print(counter)
