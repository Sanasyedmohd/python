basic_pay=float(input("Enter the basic pay:"))
hra=10/100*basic_pay
ta=5/100*basic_pay
salary=basic_pay+hra+ta
print("Basic Pay=",basic_pay)
print("HRA=",hra)
print("TA=",ta)
print("Total Salary=",salary)
