num_goods, queries = input().split(" ")
goods = [int(el) for el in input().split(" ")]

goods.sort()
sorted_prefix_sum = [0] * (int(num_goods) + 1)
for i in range(1, len(sorted_prefix_sum)):
    sorted_prefix_sum[i] = goods[i - 1] +  sorted_prefix_sum[i - 1]

for n_query in range(int(queries)):
    x_y_input = input().split(" ")
    x, y = int(x_y_input[0]), int(x_y_input[1])

    low = len(sorted_prefix_sum) - x
    end = low + (y - 1)
    print(sorted_prefix_sum[end] - sorted_prefix_sum[low - 1])