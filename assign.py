#change 80 to 89 in the list.
student_marks = [60, 80, 90, 98]
student_marks[1] = 89
print(student_marks)

#add a new item 55(append a new list).
student_marks = [60, 80, 90, 98]
student_marks.append(55)
print(student_marks)

#find the size of the list having appended
print(len(student_marks))

#write a python program to sum all the item in the list
total =sum(student_marks)
print(total)

#write a python fuction that takes two list and return, if they have atleast one python number.
list1 = input("Enter items 1;")
list2 = input("Enter items 2;")
if 60 in student_marks:
    print("yes,60 is in the list")
else:
    print("no, 60 is not in the list ")

                     