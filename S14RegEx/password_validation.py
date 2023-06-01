# Password Validation

# At least 8 characters long
# Contains lowercase and uppercase letters, numbers, #%$@
# Ends with a number

import re

pattern = re.compile(r"[a-zA-Z0-9$%#@]{7,}[0-9]$")
string = "Penguin55"

a = pattern.search(string)
print(a)
print(a.group())