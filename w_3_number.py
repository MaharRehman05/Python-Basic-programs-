n1 = int(input("Enter the number 1: "))
n2 = int(input("Enter the number 2: "))
n3 = int(input("Enter the number 3: "))
if(n1 >n2 and n1 >n3):
    print(n1,"is greater number")
elif(n2 >n1 and n2 >n3):
    print(n2,"is greater number")

elif(n3 >n1 and n3 >n2):
    print(n3,"is greater number")
else: 
    print("All are equals ")