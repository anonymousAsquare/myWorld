x = float(input('input any number: '))
y = x%2

if( x < 0 and y == 0):
    print('You entered a negative even number')
elif(x <0 and y == 1):
    print('You entered a negative odd number')
elif(x >0 and y == 0):
    print('You entered a positive even number')
elif(x > 0 and y== 1):
    print('You entered a positive odd number')
else:
    print('Zero is Neutral number')