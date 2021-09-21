# 가장 긴 감소하는 부분 수열
# 지금까지는 dp[i]가 array[i]가 마지막으로 끝나는 수로 잡고 array를 처음부터 돌면서 최신화한 반면에
# 감소하는 수열은 dp[i]가 array[i]가 시작하는 수로 잡고 array를 마지막부터 돌면서 최신화함!!!!!!!!(발상의 전환)
n = int(input())

array = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if array[i] < array[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))