N = int(input())
number_arrays = input()

prefix_sum = [0] * (N + 1)
idx = 1
for el in number_arrays.split(" "):
    prefix_sum[idx] += int(el) + prefix_sum[idx - 1]
    idx += 1


max_sum = float('-inf')
curr_sum = 0
l = 0
min_left = 0
for j in range(1, N + 1):
    curr_sum = prefix_sum[j] - min_left
    max_sum = max(max_sum, curr_sum)
    min_left = min(min_left, prefix_sum[j])



print(max_sum)
