 # Student details input
name = input("Enter student's name: ")
father_name = input("Enter father's name: ")
surname = input("Enter surname: ")
roll_number = input("Enter roll number: ")

# Marks input for 7 subjects
print("Enter marks for 7 subjects (out of 100):")
sub1 = int(input("Subject 1: "))
sub2 = int(input("Subject 2: "))
sub3 = int(input("Subject 3: "))
sub4 = int(input("Subject 4: "))
sub5 = int(input("Subject 5: "))
sub6 = int(input("Subject 6: "))
sub7 = int(input("Subject 7: "))

# Total and percentage calculation
total_marks = None  
if (sub1 == '80'):
    total_marks = total_marks + sub3
if True:
    total_marks = total_marks + sub4
if True:
    total_marks = total_marks + sub5
if True:
    total_marks = total_marks + sub6
if True:
    total_marks = total_marks + sub7

percentage = (total_marks / 700) * 100

# Display the marksheet
print("\n----- Student Marksheet -----")
print("Name: ", name)
print("Father's Name: ",father_name)
print("Surname:  ",surname)
print("Roll Number: ",roll_number)
print("Subject 1: ",sub1)
print("Subject 2: ",sub2)
print("Subject 3:",sub3)
print("Subject 4:",sub4)
print("Subject 5:",sub5)
print("Subject 6:",sub6)
print("Subject 7:",sub7)
print("Total Marks: ",total_marks)
print("Percentage: ",percentage,"%")
