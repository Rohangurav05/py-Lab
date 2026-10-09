str1="ram"
str1.split()
pal=""
for i in range(len(str1)-1,-1,-1):
    pal=pal+str1[i]
if pal==str1 :
    print("Pallindrom")
else :
    print("Not pallindrome")
