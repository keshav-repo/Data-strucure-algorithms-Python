# items[i] = [typei, colori, namei]
# items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
# ruleKey = "color"
# ruleValue = "silver"

items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"

count = 0
for item in items:
    if ruleKey == "color":
        if item[1] == ruleValue:
            count += 1
    elif ruleKey == "type":
        if item[0] == ruleValue:
            count += 1
    elif ruleKey == "name":
        if item[2] == ruleValue:
            count += 1

print(count)

