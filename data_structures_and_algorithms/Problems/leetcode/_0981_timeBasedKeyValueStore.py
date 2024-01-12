'''
datastructure -> binary search

981. Time Based Key-Value Store
Medium

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
1. TimeMap timeMap = new TimeMap();
2. timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
3. timeMap.get("foo", 1);         // return "bar"
4. timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
5. timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
6. timeMap.get("foo", 4);         // return "bar2"
7. timeMap.get("foo", 5);         // return "bar2"

1. {}
2. {"foo": ["bar", 1]} SET
3. {"foo": ["bar", 1]} GET "foo" at 1 -> "bar"
4. {"foo": ["bar", 1]} GET "foo" at 3 -> "bar"
5. {"foo": [["bar", 1], ["bar2", 4]]} SET
6. {"foo": [["bar", 1], ["bar2", 4]]} GET "foo" at 4 -> "bar2"
7. {"foo": [["bar", 1], ["bar2", 4]]} GET "foo" at 5 -> "bar2" 

Example 2:

Input
["TimeMap","set","set","get","get","get","get","get"]
[[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
Output
[null,null,null,"","high","high","low","low"]
'''

class TimeMap:
    def __init__(self):
        self.hash_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash_map:
            self.hash_map[key] = []
        self.hash_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash_map:
            return ""     
        values_lst = self.hash_map[key]
        value = self.binary_search(values_lst, timestamp)
        return value

    def binary_search(self, lst: list, target: int):
        left, right = 0, len(lst) -1
        res = ""
        while left <= right:
            mid = (left + right) // 2
            if lst[mid][0] <= target:
                res = lst[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return res