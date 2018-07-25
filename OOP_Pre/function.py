def sum(a, b):
    return a + b

a=3
b=4
c=sum(a,b)
print(c)

def say():
    return 'Hi'

a = say()
print(a)

for i in range(1, 11):
    print(a)


a = sum(3, 4)
print(a)

def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

result = sum_many(1,2,3,4,5,6,7,8,9,10)
print(result)

def sum_mul(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i

    return result

result = sum_mul('sum', 1,2,3,4,5)
print(result)
result = sum_mul('mul', 1,2,3,4,5)
print(result)

sum = lambda a, b: a+b
print(sum(3,4))

a=1
def vartest():
    global a
    a = a + 1

vartest()
print(a)

print("="*50)

def fibonacci(n):
    if n==0 or n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(3))
print("="*50)

