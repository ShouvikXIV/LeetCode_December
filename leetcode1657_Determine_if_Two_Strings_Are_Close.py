word1 = "abc"
word2 = "cba"
if(len(word1)==len(word2)):
    c = 0
    dc1 = {}
    dc2 = {}
    for i in word1:
        if i in dc1:
            dc1[i]+=1
        else:
            dc1[i] = 1
    for i in word2:
        if i in dc2:
            dc2[i]+=1
        else:
            dc2[i] = 1
    arr1 = []
    arr2 = []
    for i in dc1:
        arr3 = []
        arr3.append(dc1[i])
        arr3.append(i)
        arr1.append(arr3)
    for i in dc2:
        arr3 = []
        arr3.append(dc2[i])
        arr3.append(i)
        arr2.append(arr3)
    arr1.sort()
    arr2.sort()
    # print(arr1)
    # print(arr2)
    for i in range(len(arr1)):
        if(arr1[i][0]!=arr2[i][0]):
            break
        else:
            if(arr1[i][1] in dc2 and arr2[i][1] in dc1):
                c+=1
            else:
                break
    if(c==len(arr1)):
        print("true")
    else:
        print("false")

else:
    print("false")