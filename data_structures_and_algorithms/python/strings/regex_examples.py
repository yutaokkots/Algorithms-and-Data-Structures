import re

email_01 = 'hello@goodybye.com'
email_02 = "\'very.unusual.@.unusual.com\'@usual.com"

regex_01 = "r'@(.*)'"
regex_02 = "r'@([^@]*)$'"


def find_url01(address):
    match_address = re.search(r'@(.*)', address)
    return match_address.group(0)

a01 = find_url01(email_01)
print(a01)

def find_url02(address):
    match_address = re.search(r'@([^@]*)$', address)
    return match_address.group(0)

a02 = find_url02(email_02)
print(a02)

"""
pattern: /@([^@]*)$/gm
pattern: r'@([^@]*)$'

        \'very.unusual.@.unusual.com\'@usual.com


1) `/` : The forward slash indicates beginning of regex pattern.
2) `@` : This part of the pattern matches the literal character "@".
3) `([^@]*)` : This is a capturing group that consists of:
   `(` : The opening parenthesis starts a capturing group.
   `[^@]*` : Inside the capturing group, [^@]* matches any character except "@";
        `[^@]` - is a character class that matches any character except "@";
        `*` - indicates zero or more occurrences of the preceding character class
   `)` : The closing parenthesis ends the capturing group.
   This capturing group is used to capture any sequence of characters that are not "@" after the "@" symbol.
4) `$` : This asserts the position at the end of a line.
5) `/` : The closing forward slash indicates the end of the regular expression pattern.
6) `g` : This is a flag that stands for "global" and allows the pattern to match multiple occurrences within the input string.
7) `m` : This is a flag that stands for "multiline" and allows the pattern to match the beginning or end of each line within a multi-line input.

""" 