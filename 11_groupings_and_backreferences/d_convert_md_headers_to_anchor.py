"""Convert the given markdown headers to corresponding anchor tags. Consider the input to
start with one or more # characters followed by space and word characters. The name
attribute is constructed by converting the header to lowercase and replacing spaces with
hyphens."""

import re

header1 = "# Regular Expressions"
header2 = "## Compiling regular expressions"


def markdown_header_to_anchor(header):
    """Converts a markdown header string to an anchor tag."""
    return re.sub(
        r"\b.*",
        lambda m: f'<a name="{m[0].lower().replace(" ", "-")}"></a>{m[0]}',
        header,
    )


print(markdown_header_to_anchor(header1))
print(markdown_header_to_anchor(header2))
