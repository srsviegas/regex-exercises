# Convert the given markdown anchors to corresponding hyperlinks

import re

anchor1 = '# <a name="regular-expressions"></a>Regular Expressions'
anchor2 = '## <a name="subexpression-calls"></a>Subexpression calls'


def markdown_anchor_to_hyperlink(anchor):
    """Converts a markdown anchor string to a hyperlink"""
    return re.sub(
        r'[^"]*"(?P<name>[^"]*)".*>(?P<title>.*)', r"[\g<title>](#\g<name>)", anchor
    )


print(markdown_anchor_to_hyperlink(anchor1))
print(markdown_anchor_to_hyperlink(anchor2))
