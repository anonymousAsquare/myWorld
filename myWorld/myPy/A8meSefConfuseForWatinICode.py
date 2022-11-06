def numGrades():
    x=int(input('How many grades do you have?\n'))
    return x

def Grades(numberOfGrades):
    grades=[]
    for i in range(0,numberOfGrades,1):
        print('please input Grade', i+1)
        grades.append(float(input()))
    return grades

def printGrades(count,Array):
   # print('Your grades are:')
    for i in range (0,count,1):
        print(Array[i])
     
def average(num,Array):
    sum = 0
    for i in range(0,num,1):
        sum = sum + Array[1]
    Average = sum/num
    print('The Average of your grades is ', Average)
    return Average

def lowGrade(count,Array):
    lowGrade = 100
    for i in range(0,count,1):
        if(Array[i] < lowGrade):
            lowGrade = Array[i]
    print('Your lowest grade is ', lowGrade)
    return lowGrade

def highGrade(count,Array):
    highGrade = 0
    for i in range(0,count,1):
        if(Array[i] > highGrade):
            highGrade = Array[i]
    print('Your highest grade is ', highGrade)
    return lowGrade

def desen(count,Array):
    save = 0
    for i in range(0,count,1):
        for i in range(0,count-1,1):
            if(Array[i] < Array[i+1]):
                save = Array[i]
                Array[i] = Array[i+1]
                Array[i+1] = save
  #  print('Your Grades in desending order is')
  
def asen(count,Array):
    save = 0
    for i in range(0,count,1):
        for i in range(0,count-1,1):
            if(Array[i] > Array[i+1]):
                save = Array[i]
                Array[i] = Array[i+1]
                Array[i+1] = save
  #  print('Your Grades in asending order is')
  
numberOfGrades = numGrades()

arrayOfGrades = Grades(numberOfGrades)

print('Your Grades are: ')
printGrades(numberOfGrades,arrayOfGrades)

Average = average(numberOfGrades,arrayOfGrades)

lowGrade = lowGrade(numberOfGrades,arrayOfGrades)

highGrade = highGrade(numberOfGrades,arrayOfGrades)

desen(numberOfGrades,arrayOfGrades)
print('Your grades in desending order are:')
printGrades(numberOfGrades,arrayOfGrades)

asen(numberOfGrades,arrayOfGrades)
print('Your grades in asending order are:')
printGrades(numberOfGrades,arrayOfGrades)