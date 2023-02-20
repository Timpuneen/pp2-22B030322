#1
def kvadrati1(n):
    for i in range(n):
        yield i**2

n=int(input())
print(list(kvadrati1(n)))
#2
def eve(N):
    for i in range(1,N+1):
        if i%2==0:
            yield i

n=int(input())
print(*list(eve(n)),sep=", ")
#3
def check_check(bems):
    for i in range(bems):
        if i%3 == 0 and i%4 == 0:
            yield i

n = int(input())
print(list(check_check(n)))
#4
def kvadrati2(a,b):
    for i in range(a,b):
        yield i**2

a=int(input())
b=int(input())
for num in kvadrati2(a,b):
    print(num)
#5
def lastTask(n):
    for i in range(n,0,-1):
        yield i

n=int(input())
for zz in lastTask(n):
    print(zz)
