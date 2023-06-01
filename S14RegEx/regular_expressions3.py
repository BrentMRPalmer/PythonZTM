# Regular Expressions 3
import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = "obrentpalmer@gmail.com"

a = pattern.search(string)
print(a)
print(a.group())