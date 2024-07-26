grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students=sorted(students)
grades_mean=[]
while len(grades)>0:
    grades_mean.append(sum(grades[0]) / len(grades[0]))
    grades.remove(grades[0])

gpa={}
while len(students)>0:
    gpa.update({students.pop(0):grades_mean.pop(0)})
print(gpa)
