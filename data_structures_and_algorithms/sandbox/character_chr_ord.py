# notes from leetcode problem 2381
# 'chr()' converts unicode integer value to character
# 'ord()' converts character to unicode integer

# examples:
#chr()
for n in range(33,127):
    print(f"chr({n}) -> {chr(n)}")

# chr(33) -> !
# chr(34) -> "
# chr(35) -> #
# chr(36) -> $
# chr(37) -> %
# chr(38) -> &
# chr(39) -> '
# chr(40) -> (
# chr(41) -> )
# chr(42) -> *
# chr(43) -> +
# chr(44) -> ,
# chr(45) -> -
# chr(46) -> .
# chr(47) -> /
# chr(48) -> 0
# chr(49) -> 1
# chr(50) -> 2
# chr(51) -> 3
# chr(52) -> 4
# chr(53) -> 5
# chr(54) -> 6
# chr(55) -> 7
# chr(56) -> 8
# chr(57) -> 9
# chr(58) -> :
# chr(59) -> ;
# chr(60) -> <
# chr(61) -> =
# chr(62) -> >
# chr(63) -> ?
# chr(64) -> @
# chr(65) -> A        <-- ** chr(65) is 'A'
# chr(66) -> B
# chr(67) -> C
# chr(68) -> D
# chr(69) -> E
# chr(70) -> F
# chr(71) -> G
# chr(72) -> H
# chr(73) -> I
# chr(74) -> J
# chr(75) -> K
# chr(76) -> L
# chr(77) -> M
# chr(78) -> N
# chr(79) -> O
# chr(80) -> P
# chr(81) -> Q
# chr(82) -> R
# chr(83) -> S
# chr(84) -> T
# chr(85) -> U
# chr(86) -> V
# chr(87) -> W
# chr(88) -> X
# chr(89) -> Y
# chr(90) -> Z
# chr(91) -> [
# chr(92) -> \
# chr(93) -> ]
# chr(94) -> ^
# chr(95) -> _
# chr(96) -> `
# chr(97) -> a       <-- ** chr(97) is 'a'
# chr(98) -> b
# chr(99) -> c
# chr(100) -> d
# chr(101) -> e
# chr(102) -> f
# chr(103) -> g
# chr(104) -> h
# chr(105) -> i
# chr(106) -> j
# chr(107) -> k
# chr(108) -> l
# chr(109) -> m
# chr(110) -> n
# chr(111) -> o
# chr(112) -> p
# chr(113) -> q
# chr(114) -> r
# chr(115) -> s
# chr(116) -> t
# chr(117) -> u
# chr(118) -> v
# chr(119) -> w
# chr(120) -> x
# chr(121) -> y
# chr(122) -> z
# chr(123) -> {
# chr(124) -> |
# chr(125) -> }
# chr(126) -> ~

list_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for n in list_alpha:
    print(f"ord({n}) -> {ord(n)}")

# ord(a) -> 97
# ord(b) -> 98
# ord(c) -> 99
# ord(d) -> 100
# ord(e) -> 101
# ord(f) -> 102
# ord(g) -> 103
# ord(h) -> 104
# ord(i) -> 105
# ord(j) -> 106
# ord(k) -> 107
# ord(l) -> 108
# ord(m) -> 109
# ord(n) -> 110
# ord(o) -> 111
# ord(p) -> 112
# ord(q) -> 113
# ord(r) -> 114
# ord(s) -> 115
# ord(t) -> 116
# ord(u) -> 117
# ord(v) -> 118
# ord(w) -> 119
# ord(x) -> 120
# ord(y) -> 121
# ord(z) -> 122

## How to get the correct char
