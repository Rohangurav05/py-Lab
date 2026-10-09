str1=[1,"ram",2,"lakhan"]

num =[]
name=[]
for i in str1:
    if type(i)==int:
        num.append(i)
    else :
        name.append(i)
print("numbers : ",sorted(num,reverse=True))
print("names : ",sorted(name,reverse=True))
