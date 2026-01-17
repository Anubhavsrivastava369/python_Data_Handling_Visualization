# # i = 0
# # while i < 3:
# #     x = int(input("Enter a number : "))
# #     if (x % 2 == 0):
# #         print("You won the game")
# #         break
# #     i += 1

# # if(i == 3):
# #     print("you lost the game, Try agin")


# for e in range(1,6,2):
#     print(e,end = ' ')


# l1 = list()

# for i in range(5):
#     l1.append(input())

# print(l1)

# a = [1, 2, 3]
# b = a
# b.append(4)
# print(b)


# l1 = [1,2,3,4,4,5]

# l2 = set()

# for i in range(len(l1)):
#     l2.add(l1[i])

# print(l1)

# class Dog:
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color

#     def bark(self):
#         print(f"{self.name} dog,Had color {self.color} stark barking!")
        
# d = Dog('LabraDor','Golden')
# print(d.color)
# d.bark()


lst = ['b','c',1,1,'c','b']
lst_copy = lst.copy()
lst_copy.reverse()

if lst == lst_copy:
    print("palindrome")
else: 
    print("not palindrome")

