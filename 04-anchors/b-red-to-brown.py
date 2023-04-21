# For the given input string, change only the whole word red to brown

import re

words = "bred red spread credible red."
sub = re.sub(r"\bred\b", "brown", words)

print(sub)
