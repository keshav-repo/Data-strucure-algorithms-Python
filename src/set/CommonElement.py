ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

ar1 = set(ar1)
ar2 = set(ar2)
ar3 = set(ar3)

res = ar1.intersection(ar2)
res = res.intersection(ar3)
print(res)

