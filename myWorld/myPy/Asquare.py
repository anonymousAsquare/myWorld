import pickle
names = ['Alas', 'Jungle boi', 'Astro-bob']
num = [1,2,3]
y = 3
x = 7
t = 9
e = 4
with open('myData.pkl', 'wb') as a:
    pickle.dump(names, a)
    pickle.dump(num, a)
    pickle.dump(x, a)
    pickle.dump(y, a)
    pickle.dump(e, a)
    pickle.dump(t, a)