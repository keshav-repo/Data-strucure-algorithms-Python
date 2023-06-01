class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def __repr__(self):
        return "name: {}, height: {}".format(self.name, self.height)

names = ["Mary","John","Emma"]
heights = [180,165,170]

persons = []
for i in range(0, len(names)):
    p = Person(names[i], heights[i])
    persons.append(p)

def getKey(obj):
    return obj.height

persons.sort(key=getKey, reverse=True)

ans =[]
for prsn in persons:
    ans.append(prsn.name)
print(ans)

