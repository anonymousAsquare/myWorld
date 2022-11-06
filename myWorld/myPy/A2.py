numGrades = int(input('Please how many grades do you have: '))
Grades = []
Add = 0
lowGrade = 100
highGrade = 0
lownum = 100
#desend = 0
for i in range(0, numGrades, 1):
    count = i + 1
    print('please enter Grade: ', count)
    Grades.append(float(input('')))
print('Your grades are: ')
for i in range(0, numGrades, 1):
    print(Grades[i])
for i in range(0, numGrades, 1):
    Add = Add + Grades[i]
Average = Add/numGrades
print('The Average of your Grades is ', Average)
for i in range(0, numGrades, 1):
    if (Grades[i] < lowGrade):
        lowGrade = Grades[i]
print('Your lowest grade is ', lowGrade)    
for i in range(0, numGrades, 1):
    if (Grades[i] > highGrade):
        highGrade = Grades[i]
print('Your highest grade is ', highGrade)   
for i in range(0, numGrades-1, 1):
    for i in range(0, numGrades-1,1):
        if(Grades[i] > Grades[i+1]):
            desend = Grades[i]
            Grades[i] = Grades[i+1]
            Grades[i+1] = desend
for c in Grades:
    print(c)
    