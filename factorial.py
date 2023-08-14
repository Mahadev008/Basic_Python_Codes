# n = int(input("Enter a number: "))
# fact = 1
# for i in range(1,n+1):
#     if n < 0 :
#         print("Invalid Input")
#     elif n == 0 & n == 1 :
#         print("Factorial is 1")
#     else:
#         fact *= i
# print("factorial is" , fact)

n = int(input("Enter a number: "))
fact = 1

while n>0 :
    fact *= n
    n -= 1

print(fact)