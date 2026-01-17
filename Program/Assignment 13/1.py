# s = int(input('Enter a Number:'))
# if(s >= 100 and s <= 999):
#     print('Yess!..')
# else:
#     print('No!....')


# if(s > 0):
#  print('positive')
# elif(s == 0):
#  print('Zero')
# else:
#   print('Negative')

# print('Entre a quadratic equation value of a ,b and c..\n a^2x + bx +c')
# a,b,c = float(input('Enter 1st number:')),float(input('Enter 2st number:')),float(input('Enter 3st number:'))

# if( b*b - 4*a*c > 0):
#      print('Root are real and distinct')
# elif(  b*b - 4*a*c == 0):
#      print('Root are real and equal')
# else:
#      print('Imaginary Roots')
     

year = int(input('Enter a year:'))

if(year % 100  == 0 and year % 400 == 0 or year % 4 == 0):
     print('leap year')
else:
     print('Non leap year')


# if(a >= b and a >= c ):
#      print(a,'greater than',b,'and',c)
# elif(b >= c and b >= a):
#      print(b,'greater than',a,'and',c)
# else:
#     print(c,'greater than',a,'and',b)
     