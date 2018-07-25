print("Hello!")
print('python is fun!')
print("""Life is too short, you need python""")

print("\"Python is Easy\"")

multiline = "Life is too short\n You need Python"
print(multiline)

multiline ="""
Life is too short
You need python"""
print(multiline)

head = "Python"
tail = " is Fun"
print(head+tail)

a = "Python"
print(a*2)

print("=" * 50)
print("My Program")
print("=" * 50)

a = "Life is too short, you need python"
print(a[3])
print(a[5])
print(a[3] + a[5])

b = a[0] + a[1] + a[2] + a[3]
print(b)

print(b[:2])
print(b[2:])

print("현재 온도는 %d도입니다." % 18)
print("I eat %s apples." % "five")

number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))

print("%10s" % "hi")
print("%-10sjane" % "hi")

print("I eat {0} apples".format("five"))
print("\"파이썬\" 문제를 풀어보자.")

print("Life is too short\nYou need Python")


print("%24s" % "PYTHON")
print("%d-%d" % (881120, 1068234))

a = [1,2,3,['a','b','c']]
print(a[-1][0])

a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[2][2][0])

a = "12345"
print(a[:2])

a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)

a = [1, 2, 3]
a.append(4)
print(a)

a = [1, 4, 3, 2]
a.sort()
print(a)

a = ['a', 'c', 'b']
a.sort()
print(a)

a = ['b', 'c', 'd']
a.reverse()
print(a)

a = [1,2,3]
print(a.index(3))

a.insert(3, 5)
print(a)

a.remove(3)
print(a) #3이라는 값 삭제
print("-"*50)

a = [1,2,3]
a.pop()
print(a)
a.pop(0) #a[1]의 값 끄집어내기
print(a)

a = [1,2,3,4,5]
b = [6,7,8]
a.extend(b)
print(a)
