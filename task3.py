Name= input("Enter student's name: ")
Class= input("Enter student's class: ")
Gender= input("Enter Student's gender: ")

Subject1= 'English Language'
Score1= round(float(input("Enter score for English Language: ")))
if Score1 < 50:
    Remark1= 'FAIL'
elif Score1 == 50:
    Remark1= 'PASS'
else:
    Remark1= 'CREDIT'

Subject2= 'Mathematics'
Score2= round(float(input("Enter score for Mathematics: ")))
if Score2 < 50:
    Remark2= 'FAIL'
elif Score2 == 50:
    Remark2= 'PASS'
else:
    Remark2= 'CREDIT'

Subject3= 'General Science'
Score3= round(float(input("Enter score for General Science: ")))
if Score3 < 50:
    Remark3= 'FAIL'
elif Score3 == 50:
    Remark3= 'PASS'
else:
    Remark3= 'CREDIT'

print(f'{Name}')
print(f'{Class}')
print(f'{Gender}')
print(f'{Subject1}  {Score1} {Remark1}')
print(f'{Subject2}  {Score2} {Remark2}')
print(f'{Subject3}  {Score3} {Remark3}')