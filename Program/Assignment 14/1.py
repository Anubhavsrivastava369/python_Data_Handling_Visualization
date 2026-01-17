# x = int(input('Enter a number:'))
# match x:
#     case x if 1000 < x and x > 99:
#         print('Three digit number')
#     case x:
#         print('Not a three digit number')

# match x:
#     case x if x > 0:
#         print('Positive Number') 
#     case x if x == 0:
#         print('Negative Number')
#     case x:
#         print('zero')    

x = eval(input('Enter:'))

match x:
    case x if type(x) == int:
        print('Monday')
    case x if type(x) == float:
        print('Tuesday')
    case x if type(x) == complex:
        print('Wednesday')
    case x if type(x) == bool:
        print('Thursday')