class ReverseString():
    def reverse(self, s):
        if s == "":
            return s
        return s[-1] + self.reverse(s[:-1])
    
rev = ReverseString()
reversed_string = rev.reverse("hello there, didn't see you")
print(reversed_string)