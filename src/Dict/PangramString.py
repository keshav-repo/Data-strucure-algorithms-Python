# sentence = "thequickbrownfoxjumpsoverthelazydog"
sentence = "thequickbrownfoxjumpsoverthelazydog"
alphabets = "abcdefghijklmnopqrstuvwxyz"
dictionaryAlphabets = {}

for alphabet in alphabets:
    if alphabet in sentence:
        if alphabet in dictionaryAlphabets.keys():
            dictionaryAlphabets[alphabet] = dictionaryAlphabets[alphabet] + 1
        else:
            dictionaryAlphabets[alphabet] = 1

print(dictionaryAlphabets)

if len(dictionaryAlphabets.keys())==26:
    print("yes")
else:
    print("No")



# if dictionaryAlphabets[alphabet] < 1:
#     print('True')
# else:
#     print("False")

# x = 10
#
# x += 1
# x = x +1
#
# print(x)



