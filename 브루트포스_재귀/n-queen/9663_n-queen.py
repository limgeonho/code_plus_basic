# n-queen

def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True


def DFS(N, current_row, current_candidate):
    global final_result
    if current_row == N:
        final_result += 1
        return

    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            DFS(N, current_row + 1, current_candidate)
            current_candidate.pop()


N = int(input())
final_result = 0
DFS(N, 0, [])

print(final_result)


# def n_queens(col, i):
#     n = len(col) - 1
#     if (promising(col, i)):
#         if (i == n):
#             print(col[1: n + 1])
#         else:
#             for j in range(1, n + 1):
#                 col[i + 1] = j
#                 n_queens(col, i + 1)
#
#
# # 대각선과 같은 열에 있는 지 확인
# def promising(col, i):
#     k = 1
#     flag = True
#     while (k < i and flag):
#         if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)):
#             flag = False
#         k += 1
#     return flag
#
#
# n = int(input())
# col = [0] * (n + 1)
# n_queens(col, 0)
