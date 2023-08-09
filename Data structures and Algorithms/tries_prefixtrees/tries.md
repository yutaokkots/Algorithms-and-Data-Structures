# Tries (prefix trees, digital tree)

"Re[trie]val" -> "trie"
A trie is a variant of an n-ary tree in which characters are stored at each node. 

The idea is that all strings sharing common prefix should come from a common node.

Each path down the tree may represent a word

The * nodes (sometimes called 'null nodes') are often used to indicated complete words. 

```
               [root]
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

```
               [root]
              /      \
             a         d
            /         / \'o'
           n         a   'do'
       'd'/ \'t' 'd'/
      'and' 'ant' 'dad'
```

<table>
    <tr>
        <th>Algorithm</th>
        <th>Average</th>
        <th>Worst Case</th>
    </tr>
    <tr>
        <th>Space</th>
        <th>O(n)</th>
        <th>O(n)</th>
    </tr>
    <tr>
        <th>Search</th>
        <th>O(n)</th>
        <th>O(n)</th>
    </tr>
    <tr>
        <th>Insert</th>
        <th>O(n)</th>
        <th>O(n)</th>
    </tr>
    <tr>
        <th>Delete</th>
        <th>O(n)</th>
        <th>O(n)</th>
    </tr>
</table>
Algorithm	Average	Worst case
Space	O(n)	O(n)
Search	O(n)	O(n)
Insert	O(n)	O(n)
Delete	O(n)	O(n)