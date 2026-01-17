n = int(input("Enter a Odd number:"))

if n % 2 != 0:
    for i in range(n//2 + 1):
        for j in range(n):
            print(" ",end="")
        for j in range(n//2-i):
            print(" ",end="")
        for j in range(2*i+1):
            print("*",end="")
        print()

    for i in range(n-2):
        for j in range(n*2):
            if j == n or j == n*2 -1:
                print("@",end="")
            else:
                print(" ",end="") 
        print()


    for i in range(n//2+1):
        for j in range(n*3):
            if i == 0:
                if((j < n) or (j >= 2*n)):
                    print("*",end="") 
                elif j == n or j == 2*n - 1:
                    print("@",end="")
                else:
                    print(" ",end='')
            else:
                if  (j >= i and j <= n-i-1) :
                    print("*",end="")
                elif (j >= 2*n-1 and 
                    (j >=2*n + 2*i -i and j<= 3*n - 1 - i)):
                    print("*",end="")
                else:
                    print(" ",end="")
        print()
else:
    print("Plz enter odd number")
