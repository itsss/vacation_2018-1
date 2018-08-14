a = input()
l = len(a)

for i in a:
    l -= 1
    print('[' + i + '0'*l + ']')