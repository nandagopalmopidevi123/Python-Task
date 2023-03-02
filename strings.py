string = input("enter a string")
print(len(string))
if (len(string)) <= 2:
    print("empty string")
else:
    g=(string[0:2])
    p=(string[-2:])
    re=print(g+p)
    
#total of strings
string="12345"
total=0
for i in string:
    total=total+int(i)
print(total)   

#remove voewls
string="I am using viewing"
voewls="aeiouAEIOU"
list1=[]
for i in string:
    if i not in voewls:
        #print(i)
        list1.append(i)
print(list1)
for i in list1:
    if " " in list1:
        list1.remove(" ")
print(list1)
s="".join(list1)
print(s) 