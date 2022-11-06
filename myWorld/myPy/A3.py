numGrades = int(input('How many Grades do you have?: \n'))
Grades=[]
count = 0
while (count < numGrades):
    print('please enter Grade', count + 1)
    Grades.append(float(input('')))
    count = count + 1
count = 0
while(count < numGrades):
    print(Grades[count])
    count = count+1