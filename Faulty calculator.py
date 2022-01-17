#Faulty Calculator
num1=int(input("Enter first num:"))
num2=int(input("Enter second num"))
choose =input("Enter [+,-,*] :")
if num1==45 and num2==3 and choose=="*":
    print ("555")
elif num1== 56 and num2==9 and choose =="+":
    print ("4")
elif num1 and num2 and choose =="+":
    print(num1+num2)
elif num1 and num2 and choose =="*":
    print(num1*num2)
elif num1 and num2 and choose =="-":
    print(num1-num2)
else:
    print("Wrong input")