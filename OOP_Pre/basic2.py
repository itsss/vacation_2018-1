t1 = (1, 2, 'a', 'b')
print(t1[0])
t2 = (3, 4)
print(t1 + t2)
print(t2 * 3)

print('='*50)

dic = {'name' : 'Hong Gildong', 'phone' : '+821012345678', 'birth': '0101'}
print(dic['name'])
print(dic['birth'])
print(list(dic.keys()))

print('='*50)

s2 = set("hello")
print(s2)

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1 & s2)
print(s1 | s2)
print(s1 - s2)

s1 = set([1,2,3])
s1.remove(2)
print(s1)

print('='*50)

money = 1
if money >= 1:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

tree = 0
while tree < 10:
    tree = tree + 1
    print("나무를 %d번 찍었습니다" % tree)
    if tree == 10:
        print("나무 넘어갑니다.")

result = [90, 80, 70, 59, 55]

num = 0
for mark in result:
    num += 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % num)
    else:
        print("%d번 학생은 불합격입니다." % num)

marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number +1
    if mark < 60: continue
    print("%d번 학생 축하합니다. 합격입니다. " % number)

sum = 0
for i in range(1, 11):
    sum += i

print(sum)

print('='*50)

arr = [90, 25, 67, 45, 80]
for number in range(len(arr)):
    if arr[number] < 60: continue
    print("%d번 학생 축하합니다 합격입니다." % (number + 1))