# **Intuition**

- Use two pointers that scans a substring within string, `s`.
- Record the substring, and its frequency, inside a hashmap

<br/>

# **Approach**

### <ins>Three-steps</ins>

(1) Use a hashmap/dictionary (here called `memo`) to keep track of substrings that are encountered.

(2) Scan (loop) through the string, `s`. In a while-loop, if the proceeding (next) element is equal to the current element (*i.e.* repeating), it means that the substring is **'special'**; record the frequency (*i.e.* count) of said substring into `memo`.

(3) Finally, analyze the `memo` to find the longest substring that also has a frequency that is greater than 3.

<br/>

# **Code**

```
class Solution:
    def maximumLength(self, s: str) -> int:
        memo = {}
        r = 0

        for l in range(len(s)):
            r = l
            while r + 1 <= len(s) and s[l] == s[r]:
                memo[s[l:r + 1]] = memo.setdefault(s[l:r + 1], 0) + 1
                r += 1

        # sub-approach 1
        max_substring = 0
        
        for k, int_v in memo.items():
            if len(k) > max_substring and int_v >= 3:
                max_substring = max(max_substring, len(k))

        return max_substring if max_substring else -1

        ## OR ##################
        ## sub-approach 2
        #
        # memo_lst = sorted(memo.items(), key=lambda x: len(x[0]), reverse=True) 
        # 
        # for k, int_v in memo_lst:
        #    if int_v >= 3:
        #        return len(k)
        #
        # return -1

```

# **Complexity**

**sub-approach 1**, see below
- Time complexity:

&emsp; &emsp; &emsp; O(n<sup>2</sup>)  

- Space complexity:

&emsp; &emsp; &emsp; O(n<sup>2</sup>)

or **sub-approach 2**, see below
- Time complexity:

&emsp; &emsp; &emsp; O(n<sup>2</sup> * log(m))

- Space complexity:

&emsp; &emsp; &emsp; O(n<sup>2</sup> + m) 

<br/>

# **How it works**

## **Example**:

### **Part 1:**

`s = "aaaaa"`

Use left `l`, and right, `r` pointers:

```
""" Diagram
r = 0   # declare a right pointer, called 'r', to 0.
        ┌───┐┌───┐┌───┐┌───┐┌───┐ 
s:str = | a || a || a || a || a |
        └───┘└───┘└───┘└───┘└───┘
r     =   0
"""
```

The left pointer, `l` increments in a for-loop. Increments from `0` -> `len(s)`.

```
""" Diagram
        ┌───┐┌───┐┌───┐┌───┐┌───┐ 
s:str = | a || a || a || a || a |
        └───┘└───┘└───┘└───┘└───┘
r     =   0
l     =   0       --->        4 
"""

for l in range(len(s)):
    ...
...
```

Inside the for-loop, have a while-loop that increments `r`, as long as:
- `r` is smaller than the `len(s)` (to avoid `List Index Out of Range` error.)
- The value of s at indices `l` and `r` are the same; `s[l] == s[r]` (to ensure we only look at repeating substrings)

```
""" Diagram
        ┌───┐┌───┐┌───┐┌───┐┌───┐ 
s:str = | a || a || a || a || a |
        └───┘└───┘└───┘└───┘└───┘
r     =   0 -> 1 -> 2 -> 3 -> 4
l     =   0       --->        4 
"""

for l in range(len(s)):
    while r + 1 <= len(s) and s[l] == s[r]:
        r += 1
        ...
...
```
And inside this while loop, update the hashmap, `memo`, with the frequency of the substring that is encountered. 

```
""" Diagram
        ┌───┐┌───┐┌───┐┌───┐┌───┐ 
s:str = | a || a || a || a || a |
        └───┘└───┘└───┘└───┘└───┘
r     =   0 -> 1 -> 2 -> 3 -> 4
l     =   0       --->        4 
"""

for l in range(len(s)):
    while r + 1 <= len(s) and s[l] == s[r]:
        memo[s[l:r + 1]] = memo.setdefault(s[l:r + 1], 0) + 1
        r += 1
...
```
As a reminder, this question is asking to return:
> "the length of the longest special substring of `s` which occurs at least thrice, or `-1` if no special substring occurs at least thrice."

The hashmap, called `memo`, gives an indication of which substring occurs three times or more. 

```
# memo:
{
    'a': 4,     # <- this substring occurs three times or more
    'aa': 3,    # <- this substring occurs three times or more
    'aaa': 2, 
    'aaaa': 1
}
```

In the above case, the ***longest special substring that occurs three or more times*** is `"aa"`. (This is apparent because the length of `"aa"` is larger than the length of `"a"`, even though the frequency of `"a"` -> `4` is greater than the frequency of `"a"` -> `3`)

In order to get the longest substring there are two sub-approaches. 

<br/>

### **Part 2: Sub-approach 1**

Declare a variable called `max-substring` that will store the length of the longest substring. 

for-loop through the generated `memo` from above. In this case, iterate over `memo.items()`.

```
...
max_substring = 0

for k, int_v in memo.items():
    ...
...
```

While iterating over `memo.items()`, if the substring is greater than the current value of `max_substring` AND the frequency of said substring is greater than 3, apply Python3's `max()` function to re-record the longest substring:
```
...
max_substring = 0

for k, int_v in memo.items():
    if len(k) > max_substring and int_v >= 3:
        max_substring = max(max_substring, len(k))

return max_substring if max_substring else -1
```

Finally, return the `max_substring` if `max_substring` has value that is `not 0`/`truthy`; otherwise just return `-1` to indicate that nothing was found.

<br/>

### **Part 2: Sub-approach 2**

The hashmap, `memo`, can be ordered in the following way:

```
memo_lst = sorted(memo.items(), key=lambda x: len(x[0]), reverse=True) 
```
The above code provides a list that is sorted by the length of the keys in reverse order. 

```
# memo_lst: List[Tuple(substring:str, frequency:int)]
    [('aaaaa', 1), ('aaaa', 2), ('aaa', 3), ('aa', 4), ('a', 5)]
```
Now, just loop through this list again, and return the first item where the frequency is greater than or equal to 3. If there is no substring that meets these conditions, return -1. 

```
... 
memo_lst = sorted(memo.items(), key=lambda x: len(x[0]), reverse=True) 

for k, int_v in memo_lst:
    if int_v >= 3:
        return len(k)

return -1
```


