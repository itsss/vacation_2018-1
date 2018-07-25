def sum(a, b):
    return a+b

def safe_sum(a, b):
    if type(a) != type(b):
        print("서로 다른 객체끼리 더할 수 없습니다")
        return

    else:
        result = sum(a, b)
    return result

if __name__ == "__main__":
    print(safe_sum('a', 1))
    print(safe_sum(1, 4))
    print(sum(10, 10.4))

    #직접 파일을 실행시켰을 때만, 명령어 수행
