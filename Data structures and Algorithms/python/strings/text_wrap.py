import textwrap

quote = "So when you are listening to somebody, completely, attentively, then you are listening not only to the words, but also to the feeling of what is being conveyed, to the whole of it, not part of it."

def text_wrap(q, size):
    return textwrap.wrap(q, size)

a = text_wrap(quote, 15)
print(a)

# ['So when you are', 
# 'listening to', 
# 'somebody,', 
# 'completely,', 
# 'attentively,', 
# 'then you are', 
# 'listening not', 
# 'only to the', 
# 'words, but also', 
# 'to the feeling', 
# 'of what is', 
# 'being conveyed,', 
# 'to the whole of', 
# 'it, not part of', 
# 'it.']