""" Information about enum in Python
https://docs.python.org/3/library/enum.html

Enumeration (enum).
An enumeration is
a set of symbolic names bound to unique constant values.
         └──────┬─────┘                 └──────┬──────┘
              Cards                 SPADE, HEART, etc.

For example, in C++:

    enum Direction {North, South, East, West};

    enum Cards {Spade, Heart, Club, Diamond};

'Direction' and 'Cards' are both a data type defined by the user, 
that consists of integral constants (i.e. enumeration constants).

'North', 'South' are values of Type Direction, 
and 'Heart', 'Diamond' are values of Type Cards.

In Python:
Why enums? 
    "The properties of an enumeration are useful for defining 
    an immutable, related set of constant values 
    that may or may not have a semantic meaning." PEP 435
    e.g. There may be situations where we want to use a numeric (or string) constant.
        However, using a number directly in the source code is an anti-pattern ('magic number').
        Numbers rarely carry semantics. 
        Strings are easily confused (capitalization? spelling? snake or camel-case?)
        The following is a Fisher-Yates shuffling algorithm. 
            for i in range(1, 53):
                j = i + random.randint(0, 52 - i)
                a.swapEntries(i, j)
        What does '52' or '53' mean (to a developer)? What if we have a tarot deck of 78 cards?
        It would be naive to try to replace every instance of '52' to '78'.
        It might cause the '53' in the for-loop to be missed. 
    
When to use enums?
    "Use it anywhere you have a canonical source of enumerated data 
    in your code where you want explicitly specified to use the canonical name, 
    instead of arbitrary data.

Accessing the value in the (enum):
Cards.CLUB
Direction.WEST
or
return the printable representation  -> repr()
"""
from enum import Enum

class Cards(Enum):
    SPADE = 1
    HEART = 2
    CLUB = 3
    DIAMOND = 4

class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4

print(Cards(2))
# >>> Cards.HEART

print(Direction(3))
# >>> Direction.EAST

print(repr(Direction.NORTH))
# >>> <Direction.NORTH: 1>

for card in Cards:
    print(card)
# >>> Cards.SPADE
# >>> Cards.HEART
# >>> Cards.CLUB
# >>> Cards.DIAMOND
