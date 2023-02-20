#is_prime = lambda number: all(number%i != 0 for i in range(2, int(number**.5)+1))

# def is_prime(num):
#     if num == 1:
#         return False
#     if num > 1:
#         for j in range(2, int(num/2)+1):
#             if (num % j) == 0:
#                 return False
#         return True
#     else:
#         return True

my_list = [1,2,3,4,5,6,7,8,9,10,11]

ura_last_task = filter(lambda x: all( x%i != 0 for i in range(2, int(x**.5)+1) ), my_list)
print(list(ura_last_task))
