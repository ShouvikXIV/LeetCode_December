s = input()
dct = {}
for i in s:
    if(i in dct):
        dct[i] = dct[i]+1
    else:
        dct[i] = 1
arr = []
for i in dct:
    arr2 = []
    arr2.append(dct[i])
    arr2.append(i)
    arr.append(arr2)
arr.sort(reverse=True)
k = ""
for i in arr:
    k+=i[1]*i[0]
print(k)
# print(arr)
