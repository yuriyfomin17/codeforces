prefix_sum_array_size = int(input())
prefix_sum_array = [int(el) for el in input().split(" ")]

original_arr = [0] * (prefix_sum_array_size - 1)

for i in range(1, prefix_sum_array_size):
    original_arr[i - 1] = prefix_sum_array[i] - prefix_sum_array[i - 1]

print(" ".join([str(el) for el in original_arr]))