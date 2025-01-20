salary=int(input("enter your salary:"))
age=int(input("enter your age:"))
if(salary>=20000 or age<=25):
    loan=int(input("enter your loan amount"))
if(loan>50000):
    print("maximum loan amount is 50000")
else:
    print("you are elgible for loan")
