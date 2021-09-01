# 1
while True:
    try:
        n = int(input())
        answer = '1'
        while True:
            if int(answer) % n == 0:
                break
            else:
                answer += '1'
        print(len(answer))
    except Exception:
        break