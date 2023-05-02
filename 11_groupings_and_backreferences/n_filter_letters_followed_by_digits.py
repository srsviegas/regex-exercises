"""Filter all elements that contain a sequence of lowercase alphabets followed by '-'
followed by digits. They can be optionally surrounded by {{ and }}. Any partial match
shouldn't be part of the output."""

import re

ip = ["{{apple-150}}", "{{mango2-100}}", "{{cherry-200", "grape-87"]
filtered = [e for e in ip if re.fullmatch(r"({{)?[a-z]+-\d+(?(1)}})", e)]

print(filtered)
