import pickle
name = ['alas', 'Astro-bob', 'JungleBoi']
num = [1,2,3,4,5,6]
x = 5
y = 7
z = 9
with open('data.pkl','wb') as f:
    pickle.dump(name,f)
    pickle.dump(x,f)
    pickle.dump(z,f)
    pickle.dump(num,f)
    pickle.dump(z,f)
with open('data.pkl','rb') as a:
    y = pickle.load(a)
    b = pickle.load(a)
    c = pickle.load(a)
    d = pickle.load(a)
    e = pickle.load(a)
print(b)