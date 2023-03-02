'''print prime numbers
prime numbers in range'''

num = int(input("enter the value of num:"))
for i in range(2,num):
    if num%2 == 0 : 
        print("not prime number")
        break    
else: print(" prime")
    