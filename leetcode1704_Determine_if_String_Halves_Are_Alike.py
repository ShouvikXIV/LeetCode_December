s = input("")
k = len(s)//2
s1 = s[0:k]
s2 = s[k:]
c1 = 0
c2 = 0
for i in s1:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U"):
        c1+=1
for i in s2:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U"):
        c2+=1

print(c1 == c2)
# print(c1)
# print(c2)

# print(s1)
# print(s2)