# Regular Expressions (1 and 2)
# Not Python specific, however Python has a module for it
# Regex101.com is very useful

import re

pattern = re.compile(r"([a-zA-Z]).([a])")
string = 'search insinde of this text please!'

# print('search' in string)

# re.search(pattern, string, flags=0)
# Returns a SRE_Match object - contains a span (where it occurs in the string)
# a = re.search('this', string)
# print(a.span()) # Where the string occurs
# print(a.start()) # When the text starts
# print(a.end()) # When the text ends
# print(a.group()) # Prints the part of the string that matches (more useful with multiple searches)

a = pattern.search(string)
# b = pattern.findall(string) # Puts all instances of matches in a list
# c = pattern.fullmatch(string) # Must be the exact string
# d = pattern.match(string) # Doesn't care what comes after - only that it matches the pattern

print(a.group())