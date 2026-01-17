s = int(input("Enter a number:"))
if(s > 0):
 print('Positive nummber')
else:
 print('Non-Positive Number')

if( float(input('Enter a Number:')) % 5 == 0 ):
    print('Divisible by 5')
else:
    print('Not Divisible by 5')

x = float(input('Enter a number:'))
print('Divisible by 5' if (x) % 5 == 0 else ('Not divisible'))

print('Even' if float(input('Enter a number')) % 2 == 0 else 'Odd') 

x = float(input('Enter a number:'))
y = float(input('Enter a number:'))

if( x >= y):
    print(x,' is greatrer than ',y)
else:
    print(y,'is greatrer than',x)


# s1 = str(input('Enter 1st string:'))
# s2 = str(input('Enter 2nd string:'))

# if(s1 < s2):
#     print(s1,s2,sep='\n')
# else:
#     print(s2,s1,sep='\n')