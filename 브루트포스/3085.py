# 사탕 게임
# 시간복잡도를 미리 계산하는 습관을 기르자
# 내가 푸려고 했던 기본적인 방향은 같았음
# 전체 리스트를 순회하면서 한점과 다음 오른쪽이나 아래만 검사해도 전체 리스트를 다 확인가능하다
# 다른 두 점을 swap하고 이후에 다시 원래대로 돌려준다.
# 최대값을 갱신하면서 진행(이전과 같으면 개수누적 다르면 차음부터)
# 행 -> 열 순으로 진행하고
# 중복되는 계산을 줄이면 시간이 줄어든다(중복되는 연산을 찾아야함)n = int(input())
candy = list(input() for _ in range(n))
max_num = 0
for i in range(n-1):
    for j in range(n-1):
        if candy[i][j] != candy[i][j+1]:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            break
    cnt = 1
    for j in range(n-1):
        if candy[i][j] == candy[i][j+1]:
            cnt += 1
        max_num = max(max_num, cnt)
print(max_num)