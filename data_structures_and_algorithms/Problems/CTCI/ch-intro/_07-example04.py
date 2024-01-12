# Design an algorithm to print all permutations of a string
# for simplicity, assume all characters are unique

# consider a test spring, abcdefg
# Case: "a"     --> {"a"}
# Case: "ab"    --> {"ab", "ba"}
# Case: "abc"   --> {"abc", "acb", "cab", "cba", "bac", "bca"}
# Case: "abcd"  --> ...

# for the above example,
# "ab" -> take "a", insert "b" into every possible solution
#   ---> "a"    -> "ab", "ba"
# "abc" -> take "ab" and "ba", and insert "c" into every possible solution
#   ---> "ab"   -> "cab", "acb", "abc"
#   ---> "ba"   -> "cba", "bca", "bac"
# "abcd" -> take "cab", "acb", "abc", "cba", "bca", "bac", and insert "d" into every possible solution
#   ---> "cab"  -> "dcab", "cdab", "cadb", "cabd"
#   ---> "acb"  -> "dacb", ... etc. 
#   ---> "abc"  -> 
#   ---> "cba"  -> 
#   ---> "bca"  -> 
#   ---> "bac"  -> 


test ="abc"
class Solution():
    def str_permutation(self, perm_str):

        def recursive_perm(input):
            if len(input) == 1:
                return [input]
            permutations = []
            for i in range(len(input)):
                first_char = input[i]
                remaining_chars = input[:i] + input[i+1:]
                sub_permutations = recursive_perm(remaining_chars)

                for perm in sub_permutations:
                    permutations.append(first_char + perm)
            return permutations
        
        return recursive_perm(perm_str)

sol = Solution()
answer = sol.str_permutation(test)

print(answer)
