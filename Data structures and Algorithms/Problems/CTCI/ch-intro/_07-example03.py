# with simplify and generalize, implement a multi-stp aproach. 
# Example:

# A ransom note can be formed by cutting words out of a magazine to form a new sentence
# How would you figure out if a ransom note (represented by a string)
# can be formed from a given magazine (string)

# output is boolean

# input:
# string = "Coffee shops have become bustling hubs of social interaction, relaxation, and productivity in modern urban landscapes. With aromatic coffee wafting through the air, these establishments attract diverse clientele seeking a momentary escape from their busy lives. From the comforting ambiance to the rhythmic hum of espresso machines, coffee shops offer a haven for conversation, study, or quiet introspection. Baristas craft intricate latte art, adding an artistic touch to the frothy beverages. Patrons often find themselves engrossed in novels, laptops, or engaging in lively discussions. These vibrant spaces cultivate a sense of community, fostering connections among strangers who bond over shared love for the bean-to-cup journey."
# target = "Coffee shops offer aromatic beverages, relaxation, social connections, latte art, and a bustling ambiance"
# incorrect = "There is a note that can be made from the paragraph"

string = "Coffee shops have become bustling hubs of social interaction, relaxation, and productivity in modern urban landscapes. With aromatic coffee wafting through the air, these establishments attract diverse clientele seeking a momentary escape from their busy lives. From the comforting ambiance to the rhythmic hum of espresso machines, coffee shops offer a haven for conversation, study, or quiet introspection. Baristas craft intricate latte art, adding an artistic touch to the frothy beverages. Patrons often find themselves engrossed in novels, laptops, or engaging in lively discussions. These vibrant spaces cultivate a sense of community, fostering connections among strangers who bond over shared love for the bean-to-cup journey."
target = "Coffee shops offer aromatic beverages, relaxation, social connections, latte art, and a bustling ambiance"
incorrect = "There is a note that can be made from the paragraph"
class Solution():
    def cut_word(self, sentence: str, target: str) -> bool:
        sentence = sentence.replace(",","")
        sentence = sentence.replace(".","").lower()
        target = target.replace(",","").lower()

        input_lst = sentence.split(" ")
        target_lst = target.split(" ")
        print(input_lst)
        print(target_lst)
        for word in target_lst:
            if word not in input_lst:
                return False
    
        return True
    
sol = Solution()
answer = sol.cut_word(string, target)
answer2 = sol.cut_word(string, incorrect)
print(answer)
print(answer2)

