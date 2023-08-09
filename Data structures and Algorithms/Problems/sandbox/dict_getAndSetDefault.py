students = {
    "richard": {"math": 100, "verbal": 90},
    "alice": {"math": 90, "verbal": 95}
}

print(students["richard"])
# {'math': 100, 'verbal': 90}

# dict.get(key, return)
# if the key is not in the dictionary, then returns the item in the second parameter
result = students.get("leon", {"math": 99, "verbal": 89})
print(result)
print(students)
# does not modify the original dictionary

# if the key is not in the dictionary, then sets the default value, and returns the reference to the new item
result = students.setdefault("jon", {"math": 95, "verbal": 92})
print(result)
print(students)
# modifies the original dictionary
#   students = {
#       'richard': {'math': 100, 'verbal': 90}, 
#       'alice': {'math': 90, 'verbal': 95}, 
#       'jon': {'math': 95, 'verbal': 92}
#   }


# to create a key:value pair memo for frequency of elements in a list
memo = {}
scores = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5]

for i in range(len(scores)):
    memo.setdefault(scores[i], 0)
    memo[scores[i]] += 1

print(memo)
# {1: 5, 2: 4, 3: 3, 4: 2, 5: 1}


s = "anagram"
countS = {}



#when i = 2
for i in s:
    countS[s[i]] = 1 + countS.get(s[i], 0)
    print(countS)


print(countS)

countS = {
    "a": 5,
    "b": 5,

}