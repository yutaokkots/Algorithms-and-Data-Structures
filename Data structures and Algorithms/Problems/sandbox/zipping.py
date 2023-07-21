#zipping two different lists together

english = ["namaste", "please", "thank you"]
hindi= ["नमस्ते", "कृप्या", "धन्यवाद"]
hindi_2= ["नमस्ते", "कृप्या"]
order = [52, 54, 12]
order_2 = [52, 54, 12, 16, 23, 34]

zipped_product = zip(english, hindi)

list_zipped_product = list(zipped_product)

#appears you cannot access a zipped object directly. 
# for vocab in zipped_product:
#     eng_word, hindi_word = vocab
#     print(f"the english word for {eng_word} in Hindi is {hindi_word}")

for vocab in list_zipped_product:
    eng_word, hindi_word = vocab
    print(f"the english word for {eng_word} in Hindi is {hindi_word}")

print(list_zipped_product)

for n in range(0, len(list_zipped_product)):
    eng_word, hindi_word = list_zipped_product.pop()
    print(f"{hindi_word} is of the type, {type(hindi_word)}")
    print(f"the english word for {eng_word} in Hindi is {hindi_word}")

print(list_zipped_product)

print("\n- - - - - - - -\n")

## can I zip three lists? YES
zipped_product = zip(english, hindi, order)
print(zipped_product)           # <zip object at 0x1081ad800>
print(type(zipped_product))     # <class 'zip'>
print(list(zipped_product))     # [('namaste', 'नमस्ते', 52), ('please', 'कृप्या', 54), ('thank you', 'धन्यवाद', 12)]

## can I zip two lists that are not the same length?
zipped_product_2 = zip(english, hindi_2, order_2)
print(zipped_product_2)         # <zip object at 0x1081ad800>
print(type(zipped_product_2))   # <class 'zip'>
print(list(zipped_product_2))   # [('namaste', 'नमस्ते', 52), ('please', 'कृप्या', 54)]
# yes, but it is as long as the shortest list that is zipped

