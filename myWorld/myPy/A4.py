numGrades = int(input('How many grades do you have?: '))
Grades = []
for i in range(0,numGrades,1):
    y = i+1
    print('please enter Grade', y)
    Grades.append(float(input('')))
i = 0
for i in range(0,numGrades,1):
    print(Grades[i])
#Average = (Grades[i]+Grades[i+1]+...)/numGrades
i = 0
Add = 0
for i in range(0,numGrades,1):
    Add = Add + Grades[i]
Average = Add/numGrades
print('The Average of your grades is ',Average)
i = 0
lowGrade = 100
for i in range(0,numGrades,1):
    if (Grades[i] < lowGrade):
        lowGrade = Grades[i]
print('Your lowest Grade is ', lowGrade)
i = 0
highGrade = 0
for i in range(0,numGrades,1):
    if (Grades[i] > highGrade):
        highGrade = Grades[i]
print('Your highest Grade is ', highGrade)
i = 0
hold = 0
for i in range(0, numGrades, 1):
    for i in range(0,numGrades-1,1):
        if(Grades[i] < Grades[i+1]):
            hold = Grades[i]
            Grades[i] = Grades[i+1]
            Grades[i+1] = hold
print('Your Grades in desending order are ')
i = 0
for i in Grades:
    print(i)
i = 0
hold = 0
for i in range(0, numGrades, 1):
    for i in range(0,numGrades-1,1):
        if(Grades[i] > Grades[i+1]):
            hold = Grades[i]
            Grades[i] = Grades[i+1]
            Grades[i+1] = hold
print('Your Grades in asending order are ')
i = 0
for i in Grades:
    print(i)