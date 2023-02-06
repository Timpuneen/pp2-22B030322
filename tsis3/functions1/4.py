#isPrime=lambda x: all(x % i != 0 for i in range(int(x**0.5)+1)[2:])

def isPrime(check_num):
    if check_num==1:
        return False
    if check_num > 1:
        for j in range(2, int(check_num/2)+1):
            if (check_num % j) == 0:
                return False
        return True
    else:
        return True

def filter_prime(my_list):
    result = []
    for iter in my_list:
        if isPrime (int(iter)):
            result.append((iter))
    return result
            

my_list = input().split(' ')
print((filter_prime(my_list)))
