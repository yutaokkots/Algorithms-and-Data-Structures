# **Hashtables**

a hash function maps strings to numbers. 

i.e. hash maps, maps, dictionaries, associative arrays

other examples:

mapping a web address to an IP address -> process is called DNS resolution. 

hash function tells you exactly where value is stored

```
 ________ ________ ________ ________ ________
|        |        |        |        |        | 
|  1.49  |  0.79  |  2.49  |  0.67  |  1.49  | 
|________|________|________|________|________|
     0        1        2        3        4

"apple" --> hash_function --> index 3 --> 0.67
"milk"  --> hash_function --> index 0 --> 1.49
```

* hash function consistently maps a name to the same index
* hash function maps different strings to different indices
* hash function knows how big your array is and only returns valid indexes

## in Python:
```
book = dict()

book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.49

print(book)
>>> {'apple': 0.67, 'milk': 1.49, 'avocado': 1.49}
```

# Dictionaries in python

All of the following create the same dictionary:

```
d = {
  "one":1
  "two":2
  "three":3
}
```

***Doesn't require declaring the keys as strings:***
```
a = dict(one=1, two=2, three=3)
```

***Most common way to create dictionary, and comparable to objects in javascript:***
```
b = {'one': 1, 'two': 2, 'three': 3}
```

***Zipping two lists together:***
```
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
```

***Creating a dictionary from a sset of tuples:***
```
d = dict([('two', 2), ('one', 1), ('three', 3)])
```

***Using dict() to create a dictionary {}:***
```
e = dict({'three': 3, 'one': 1, 'two': 2})
```
***Mixing up different formats:***
```
f = dict({'one': 1, 'three': 3}, two=2)
```

```
>>> print(a == b == c == d == e == f)
>>> True
```