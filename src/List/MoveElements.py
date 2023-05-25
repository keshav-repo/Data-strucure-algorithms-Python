list = [-12, 11, -13, -5, 6, -7, 5, -3, -6]

def swap(a, b):
    temp = list[a]
    list[a] = list[b]
    list[b] = temp

last = len(list) - 1
first = 0
while last > first:
    if list[first] <0:
        first = first + 1
    else:
        swap(first, last)
        last = last-1

print(list)
