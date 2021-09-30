# 오름세
# 테스트케이스가 주어지지 않은경우에는 try except를 통해서 EOF처리를 해준다!!

from bisect import bisect_left

while True:
    try:
        n = int(input())
        array = list(map(int, input().split()))

        dp = [array[0]]

        for i in range(1, n):
            if dp[-1] < array[i]:
                dp.append(array[i])
            else:
                dp[bisect_left(dp, array[i])] = array[i]
        print(len(dp))

    except:
        break
