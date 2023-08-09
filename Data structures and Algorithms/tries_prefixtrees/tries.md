# Tries (prefix trees)

A trie is a variant of an n-ary tree in which characters are stored at each node. 

Each path down the tree may represent a word

The * nodes (sometimes called 'null nodes') are often used to indicated complete words. 

```
                [ ]
              /  |  \
             M   L   A
           / |    \   \
         A   Y     I   *
        /    |      \   
       N     *       E
      / \            |
     Y   *           *
     |
     *
```

Very commonly, a trie is used to store the entire (English) language for quick prefix lookups

A hash table can quickly look up whether a string is a valid word, 
but it cannot tell us if a string is a prefix of any valid word. 

A trie can check if a string is a valid string in O(K) time, where K is the length of the string. 
