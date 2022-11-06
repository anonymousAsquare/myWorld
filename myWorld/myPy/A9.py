class students:
    def __init__(self):
        self.firstName = input('Please Enter student first name: \n')
        self.lastName = input('Please Enter '+         self.firstName+' last name: \n')
        self.numGra = int(input('How many grades does '+self.firstName+' Has?: \n'))
        
    def inputGrades(self,):
        self.grades = []
        i = 1
        while(i <= self.numGra):
            print('Entet grade ',i)
            self.grades.append(float(input()))
            i = i+1
        
    def printGrades(self):
        print(self.firstName, 'Grades are:')
        for i in self.grades:
            print(i)
            
    def average(self):
        sum=0
        for i in range(0,self.numGra,1):
            sum = sum + self.grades[i]
        average = sum/self.numGra
        print('The Average of '+self.firstName+' Grades is ', average)
        
    def hLestGrade(self):
        high = 0
        low = 100
        for i in range(0, self.numGra,1):
            if(self.grades[i] > high):
                high = self.grades[i]
            if(self.grades[i] < low):
                low = self.grades[i]
        print(self.firstName+' higest Grade is ', high)
        print(self.firstName+' lowest Grade is ', low)
        
    def deOrder(self):
        hold = 0
        for i in range(0,self.numGra,1):
            for i in range(0,self.numGra-1,1):
                if(self.grades[i] < self.grades[i+1]):
                    hold = self.grades[i]
                    self.grades[i] = self.grades[i+1]
                    self.grades[i+1] = hold
        print('Your grades in desending order is')
        for i in self.grades:
                print(i)
                
    def asOrder(self):
        hold = 0
        for i in range(0,self.numGra,1):
            for i in range(0,self.numGra-1,1):
                if(self.grades[i] > self.grades[i+1]):
                    hold = self.grades[i]
                    self.grades[i] = self.grades[i+1]
                    self.grades[i+1] = hold
        print('Your grades in asending order is')
        for i in self.grades:
                print(i)
    
 
x = []
numStu = int(input('How many students do you have? \n'))
for i in range(0,numStu,1):
    print('Student', i+1)
    y = input('Please enter student name: ')
    x.append(y)
    x[i] = students()
    x[i].inputGrades()

z = input('What students data do you need? ')
for i in range(0, numStu,1):
    if (z == x[i]):
        .printGrades()
#Geo = students()
#Geo.inputGrades()
#Geo.printGrades()
#Geo.average()
#Geo.hLestGrade()
#Geo.asOrder()
#Geo.deOrder()