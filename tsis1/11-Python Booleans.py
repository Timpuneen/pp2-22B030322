print(10 > 9)#T
print(10 == 9)#F
print(10 < 9)#F
#----------
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")#+
#----------
print(bool("Hello"))#T
print(bool(15))#T
#----------
x = "Hello"
y = 15

print(bool(x))#T
print(bool(y))#T
#----------
bool("abc")#T
bool(123)#T
bool(["apple", "cherry", "banana"])#T
#----------
bool(False)#F
bool(None)#F
bool(0)#F
bool("")#F
bool(())#F
bool([])#F
bool({})#F
#----------
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))#F
#----------
def myFunction() :
    return True

print(myFunction())#T
#----------
def myFunction() :
    return True

if myFunction():
    print("YES!")#+
else:
    print("NO!")
#----------
x = 200
print(isinstance(x, int))#T
#Exercises:
"""
1-True
2-False
3-False
4-True
5-False
"""