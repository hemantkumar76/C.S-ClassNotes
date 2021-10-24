i = int(input("Enter the no of iterations: "))
for x in range(i,1,-1):
     for j in range(0,x+1):
           print("*",end=" ")
     print("\r")
print("*")
