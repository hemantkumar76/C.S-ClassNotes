i = int(input("Enter the no of iterations: "))
for x in range(i,1,-1):
     for _ in range(x+1):
          print("*",end=" ")
     print("\r")
print("*")
