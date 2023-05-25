num = [1,2,3,4]

num2 = [  [1, 2, 3, 4],
          [10,11,14,15],
          [50,51,52,52]]

#print(num2)

# print(num2[1][2])
#
# print(num2[2][3])
#
#
# print(len(num2))

#print(  len( num2[0] ))


for row in range(0, len(num2)):
    for col in range(0, len(num2[0])):
        print(num2[row][col], end=" ")
    print("")


