class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def __init__(self):
        self.key = "&$*@#"
    def encode(self, strs):
        # write your code here
        print(strs)
        return self.key.join(strs)

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        print(str)
        return str.split(self.key)

ex_1 = ["lint","code","love","you"]
ex_2 = ["we", "say", ":", "yes"]

sol1 =  Solution()
enc_1 = sol1.encode(ex_1)
print(sol1.decode(enc_1))

sol2 =  Solution()
enc_2 = sol2.encode(ex_2)
print(sol2.decode(enc_2))
