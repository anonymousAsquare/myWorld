import pickle
with open('gra.pkl', 'rb') as j:
    c = pickle.load(j)
    a = pickle.load(j)
    b = pickle.load(j)
z = 0
while(z<c):
    print('What student Average do you want? ')
    x = input('')
    for i in range(0,c,1):
        if(x == a[i]):
            print(x+"'s Average is ", b[i])
    z=z+1      
print('Thats all')