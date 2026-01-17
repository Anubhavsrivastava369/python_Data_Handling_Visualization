x = int(input("Enter a number : "))
# for i in range(1,x):
#     for j in range(1,x):
#         if(j >= x-i):
#             print("*",end='')
#         else:
#             print(" ",end='')
#     print()
        

# for i in range(1,x):
#     for j in range(1,x):
#         if j <= x - i:
#             print("*",end='')
#         else:
#             print(" ",end="")
#     print()

# for i in range(1,5):
#     for j in range(1,5):
#         if j >= i:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# if x % 2 != 0 :
#     for i in range(1,int(x/2 + 1)+1):
#         a = int(x/2 + 1)
#         for j in range(1,x+1):
#             if (j<=a-i or j> a+i-1):
#                 print(" ",end="")
#             else:
#                 print("*",end="")
#         print()
# else:
#     print("Enter odd number")


# if x % 2 != 0:
#     for i in range(1,int(x/2 + 1)+1):
#         for j in range(1,x+1):
#             if j >= i and j <=  x-i+1:
#                 print("*",end="")
#             else:
#                 print(" ",end="") 
#         print()


if x % 2 != 0:
    for i in range(1,int(x/2 + 1)+1):
        a = int(x/2 + 1)
        for j in range(1,x+1):
            if j <= a-i+1 or j >= a+i-1:
                print("*",end="")
            else:
                print(" ",end="")
        print()