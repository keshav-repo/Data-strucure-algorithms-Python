input = "characters"
dub = {}

size = len(input)
for i in range(0, size):
    ch = input[i]
    if ch in dub.keys():
        dub[ch] = True
    else:
        dub[ch] = False

for key in dub.keys():
    if dub[key] == True:
        print(key, end=",")
