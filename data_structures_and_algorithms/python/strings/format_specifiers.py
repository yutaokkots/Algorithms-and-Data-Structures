'''
older versions of string formatting (before Python 2.6)
%d  ...... decimals
%f  ...... float
%s  ...... string

d	Signed integer decimal.
i	Signed integer decimal.
o	Unsigned octal.
u	Obsolete and equivalent to 'd', i.e. signed integer decimal.
x	Unsigned hexadecimal (lowercase).
X	Unsigned hexadecimal (uppercase).
e	Floating point exponential format (lowercase).
E	Floating point exponential format (uppercase).
f	Floating point decimal format.
F	Floating point decimal format.
g	Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise.
G	Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise.
c	Single character (accepts integer or single character string).
r	String (converts any python object using repr()).
s	String (converts any python object using str()).
%	No argument is converted, results in a "%" character in the result.

'''
name = "Gandalf"
extendedName = "the Grey"
age = 84
iq = 149

######## OUTDATED STRING FORMATTING

print('%s %s\'s age is %d with incredible IQ of %f ' %(name, extendedName, age, iq)) 
# Gandalf the Grey's age is 84 with incredible IQ of 149.900000

dict = {
    "%d":"{}",
    "%i":"{}",
    "%o":"{}",
    "%u":"{}",
    "%x":"{}",
    "%X":"{}",
    "%e":"{}",
    "%E":"{}",
    "%f":"{}",
    "%F":"{}",
    "%g":"{}",
    "%G":"{}",
    "%c":"{}",
    "%r":"{}",
    "%s":"{}",
    "%%":"%"
}