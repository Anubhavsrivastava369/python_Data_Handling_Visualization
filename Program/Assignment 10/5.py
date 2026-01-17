a = input('Enter a number:')
if(len(a) % 2 == 0):
    print(a[int(len(a)/2-1)])
else:
    print(a[int(len(a)/2)])
 