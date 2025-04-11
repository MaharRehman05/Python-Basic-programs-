name = input("Enter Your  name : ")
f_name = input("Enter Your Father name:  ")
s_name = input("Enter Your surname : ")
Roll_no = int(input("Enter your Roll no: "))
sub1 = int(input("Enter subject1 marks: "))
sub2 = int(input("Enter subject2 marks: "))
sub3 = int(input("Enter subject3 marks: "))
sub4 = int(input("Enter subject4 marks: "))
sub5 = int(input("Enter subject5 marks: "))
sub6 = int(input("Enter subject6 marks: "))
sub7 = int(input("Enter subject7 marks: "))

total_marks = sub1+ sub2+ sub3+ sub4+sub5+ sub6+ sub7
percentage = (total_marks/700)*100


print("-------Student Marksheet----------")
print("Name : ", name)
print("Father Name : ", f_name)
print("Surname : ", s_name)
print("Roll No:", Roll_no)
print("Subbject 1 marks : ", sub1)
print("Subbject 2 marks : ", sub2)
print("Subbject 3 marks : ", sub3)
print("Subbject 4 marks : ", sub4)
print("Subbject 5 marks : ", sub5)
print("Subbject 6 marks : ", sub6)
print("Subbject 7 marks : ", sub7)
print("Total  Marks : ", total_marks)
print("Percentage :  ", percentage, "%")


if percentage >= 90:
    print("Grade: A+")
if percentage >= 80 and percentage < 90:
    print("Grade: A")
if percentage >= 70 and percentage < 80:
    print("Grade: B")
if percentage >= 60 and percentage < 70:
    print("Grade: C")
if percentage >= 50 and percentage < 60:
    print("Grade: D")
if percentage < 50:
    print("Grade: Fail")