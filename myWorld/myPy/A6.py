import pickle 
numStu = int(input('How many Students do you have?\n'))
name = []
nameGra = []
for i in range(0,numStu,1):
     y = i + 1
     print('please whats the name of student ', y," ?")
     name.append(input())
     print('whats the average score of', name[i])
     nameGra.append(float(input('')))
with open('gra.pkl', 'wb') as j:
         pickle.dump(numStu,j)
         pickle.dump(name, j)
         pickle.dump(nameGra,j)
with open('gra.pkl', 'rb') as j:
    c = pickle.load(j)
    a = pickle.load(j)
    b = pickle.load(j)
print('What student Average do you want? ')
x = input('')
for i in range(0,numStu,1):
    if(x == a[i]):
        print(x+"'s Average is ", b[i])



        