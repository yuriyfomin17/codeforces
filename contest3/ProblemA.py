array_size = int(input())
array = [int(el) for el in input().split(" ")]

prefix_sum_arr = [0] * (array_size + 1)

for i in range(1, len(prefix_sum_arr)):
    prefix_sum_arr[i] = prefix_sum_arr[i - 1] + array[i - 1]

print(" ".join([str(el) for el in prefix_sum_arr]))
