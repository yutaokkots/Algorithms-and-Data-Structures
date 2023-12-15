import re

string_01 = "\'very.unusual.@.unusual.com\'@usual.com"

substr = re.search(r'([^@]*)', string_01)

"""
r'@([^@]*)$'


               15             30
               │              │                       
\'very.unusual.@.unusual.com\'@usual.com
│         │         │         │        │      
0         10        20        30       39


                                                substr.group(0)                 substr
substr = re.search(r'@', string_01)             @                               <re.Match object; span=(14, 15), match='@'>
substr = re.search(r'@()$', string_01)          ERROR                           None
substr = re.search(r'@(.)', string_01)          @.                              <re.Match object; span=(14, 16), match='@.'>
substr = re.search(r'@(.*)', string_01)         @.unusual.com'@usual.com        <re.Match object; span=(14, 38), match="@.unusual.com'@usual.com">
substr = re.search(r'@([^@])', string_01)       @.                              <re.Match object; span=(14, 16), match='@.'>
substr = re.search(r'@([^@]*)', string_01)      @.unusual.com'                  <re.Match object; span=(14, 28), match="@.unusual.com'">
substr = re.search(r'@([^@]*)$', string_01)   > @usual.com                      <re.Match object; span=(28, 38), match='@usual.com'>
substr = re.search(r'@(.*)$', string_01)        @.unusual.com'@usual.com        <re.Match object; span=(14, 38), match="@.unusual.com'@usual.com">
substr = re.search(r'(.*)@', string_01)         'very.unusual.@.unusual.com'@   <re.Match object; span=(0, 29), match="'very.unusual.@.unusual.com'@">
substr = re.search(r'([^@]*)', string_01)       'very.unusual.                  <re.Match object; span=(0, 14), match="'very.unusual.">


asterisk (*) is a quantifier that specifies "zero or more occurrences" of the preceding character or group.
the anchor ($) asserts the position at the end of a line.
"""

print(substr)
print(substr.group(0))

second_substr01 = re.search(r'end$' ,"The end is near")     # None
second_substr02 = re.search(r'end$' ,"This is the end")     # <re.Match object; span=(12, 15), match='end'>
second_substr03 = re.search(r'end$' ,"End of the road")     # None
second_substr04 = re.search(r'end$' ,"Not the end")         # <re.Match object; span=(8, 11), match='end'>

