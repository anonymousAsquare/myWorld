import pickle
with open('gra.pkl', 'rb') as j:
    a = pickle.load(j)
    b = pickle.load(j)
print('What student Average do you want? ')
x = input('')
for i in range(0,numStu,1):
    if(x == a[i]):
        print(x+"'s Average is ", b[i])
