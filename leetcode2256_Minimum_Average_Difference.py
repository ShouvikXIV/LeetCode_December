nums = [2,5,3,9,5,3]
nums2 = []
nums2.append(nums[0])
i = 1
while(i<len(nums)):
    nums2.append(nums[i]+nums2[i-1])
    i+=1

arr = []
c = len(nums2)-1
for i in range(len(nums2)):
    a = nums2[i]//(i+1)
    b = nums2[-1]-nums2[i]
    if b == 0 and c == 0:
        arr.append(abs(round(a)))
    else:
        arr.append(abs(round(a-(b//c))))  
    c-=1
d = min(arr)

for i in range(len(arr)):
    if arr[i]==d:
        print(i)
        break
