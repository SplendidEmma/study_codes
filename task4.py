Name = input("Enter student's full name: ")
Class = input("Enter student's class: ")

Subject1 = input("Enter first subject: ")
Score1 = round(float(input(f"Enter score for {Subject1}: ")))

Subject2 = input("Enter second subject: ")
Score2 = round(float(input(f"Enter score for {Subject2}: ")))

Subject3 = input("Enter third subject: ")
Score3 = round(float(input(f"Enter score for {Subject3}: ")))

Subject4 = input("Enter forth subject: ")
Score4 = round(float(input(f"Enter score for {Subject4}: ")))

Subject5 = input("Enter fifth subject: ")
Score5 = round(float(input(f"Enter score for {Subject5}: ")))

Total = (Score1 + Score2 + Score3 + Score4 + Score5)
Average = ((Total)/5)
if Average >= 70:
    Remark = 'Distinction'
elif Average >= 60  <= 69:
    Remark = 'Merit'
elif Average >= 50  <= 59:
    Remark = 'Credit'
else:
    Remark = 'Fail'

print("-------------------Student's Result-------------------------")
print("")
print(f"Name: {Name}")
print(f"Clas: {Class}")
print("") # make a space
print(f"{Subject1}     {Score1}")
print(f"{Subject2}     {Score2}")
print(f"{Subject3}     {Score3}")
print(f"{Subject4}     {Score4}")
print(f"{Subject5}     {Score5}")
print("")
print(f"Total Score: {Total}")
print(f"Average: {Average}")
print(f"Remark: {Remark}")
print("")
print("------------------------------------------------------------")


