
# Python Data Types Overview

<table>
    <tr>
        <th>Type</th>
        <th>Name</th>
        <th>Typing</th>
        <th>Function</th>
        <th>Example</th>
        <th>Immutability</th>
    </tr>
    <tr>
        <td>numeric</td>
        <td>Integer</td>
        <td>int</td>
        <td>int(value, base(opt, default=10))</td>
        <td>n = 5</td>
        <td>immutable</td>
    </tr>
    <tr>
        <td>numeric</td>
        <td>Floating point</td>
        <td>float</td>
        <td>float(value)</td>
        <td>pi = 3.14</td>
        <td>immutable</td>
    </tr>
    <tr>
        <td>numeric</td>
        <td>Complex</td>
        <td>complex</td>
        <td>complex(real, imaginary(opt))</td>
        <td>z1 = 2 + 3j</td>
        <td>immutable</td>
    </tr>
    <tr>
        <td>text</td>
        <td>String</td>
        <td>str</td>
        <td>str(object, encoding(opt), errors(opt))</td>
        <td>s = "hello"</td>
        <td>immutable</td>
    </tr>
    <tr>
        <td>text</td>
        <td>Bytes</td>
        <td>bytes</td>
        <td>bytes(object, encoding(opt), errors(opt))</td>
        <td>binary_data = b'\\\\\\\\x48\\\\\\\\x65
        \\\\\\\\x6c\\\\\\\\x6c\\\\\\\\x6f'</td>
        <td>immutable</td>
    </tr>
    <tr>
        <td>text</td>
        <td>Byte Arrays</td>
        <td>bytearray</td>
        <td>bytearray(source(opt), encoding(opt), errors(opt))</td>
        <td>mutable_data = bytearray(b'\\\\\\\\x48\\\\\\\\x65
        \\\\\\\\x6c\\\\\\\\x6c\\\\\\\\x6f')</td>
        <td>mutable</td>
    </tr>
    <tr>
        <td>sequence</td>
        <td>List</td>
        <td>list</td>
        <td>list(), []</td>
        <td>fruits = ["apple", "banana", "orange"]</td>
        <td>mutable</td>
    </tr>
    <tr>
        <td>sequence</td>
        <td>Tuple</td>
        <td>tuple</td>
        <td>tuple(), ()</td>
        <td>point = (1, 2)</td>
        <td>immutable</td>
    </tr>
    <tr>
        <td>sequence</td>
        <td>Range</td>
        <td>range</td>
        <td>range(start(opt), stop(opt), step(opt))</td>
        <td>range(2,5)</td>
        <td>immutable</td>
    </tr>
    <tr>
        <td>mapping</td>
        <td>Dictionary</td>
        <td>dict</td>
        <td>dict(**kwargs), {}</td>
        <td>dict("first"=2,"second"=5)</td>
        <td>mutable</td>
    </tr>
    <tr>
        <td>mapping</td>
        <td>Set</td>
        <td>set</td>
        <td>set(*args)</td>
        <td>new_set = set([1,2,3]) ## True and 1 are same</td>
        <td>mutable</td>
    </tr>
    <tr>
        <td>mapping</td>
        <td>Frozen Set</td>
        <td>frozenset</td>
        <td>frozenset(iterable)</td>
        <td>immutable_set = frozenset([1,2,3])</td>
        <td>immutable</td>
    </tr>
</table>

# Python Data Structure Calls

<table>
    <tr>
        <td>Heap</td>
        <td>heapq</td>
        <td>import heapq</td>
        <td></td>
    </tr>
    <tr>
        <td>Double ended queue</td>
        <td>deque</td>
        <td>from collections import deque</td>
        <td></td>
    </tr>
    <tr>
        <td>Double ended queue</td>
        <td>deque</td>
        <td>from collections import deque</td>
        <td></td>
    </tr>
</table>
