# n = int(input())
# tmp = [i for i in range(100) if i % 2 != 0]
# line_len = tmp[n - 1]
# for i in range(n):
#     print(f"{'#' * tmp[i]}".center(line_len))

n = int(input()) * 2
for i in range(1, n, 2):
    print(('#' * i).center(n - 1))
