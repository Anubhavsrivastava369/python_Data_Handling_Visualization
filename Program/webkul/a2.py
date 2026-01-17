# n = 5
# for i in range(n-1):
#     for j in range(n):
#         if j < n-i:
#             print(" ",end="")
#     for j in range(2*i + 1):
#         print("@",end="")
#     print()

# for i in range(n):
#     if i < n//2:
#         for j in range(2*n):
#             if (j >= n//2 - i and j <= n//2) or (j >= 2*n - n//2 and j <= 2*n - n//2 + i):
#                 print("*",end="")
#             else:
#                 print(" ",end="")
#         print()
#     elif i == n//2:
#         for j in range(2*n+1):
#             if j >= n - n//2 and j <= n + n//2:
#                 print("@",end="")
#             else:
#                 print("*",end="")
#         print()

# for i in range(n//2):
#     for j in range(2*n):
#         if (j >=i+1 and j <= n//2) or (j >= 2*n - n//2 and j <= 2*n - 2*i) :
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()


n = 7

for i in range(n//2+1):
    for j in range(n//2 + i):
        print(" ",end="")
    for j in range(n//2 + n):
        if j >= n//2 + i:
            if j < n//2 + n -i :
                print("@",end="")
    print() 

for i in range(n):
    for j in range(n):
        if i == 0 or (j == 0 or j == n-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
