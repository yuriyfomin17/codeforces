array_size, number_of_queries = input().split(" ")
array_str = input()

prefix_sum = [0] * (int(array_size) + 1)
idx = 1
for el in array_str.split(" "):
    prefix_sum[idx] += int(el) + prefix_sum[idx - 1]
    idx += 1

for query_n in range(int(number_of_queries)):
    l, r = input().split(" ")
    print(prefix_sum[int(r)] - prefix_sum[int(l)  - 1])