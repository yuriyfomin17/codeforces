
num_rows, num_columns = map(int, input().split(" "))

matrix = []
for _ in range(num_rows):
    matrix.append([int(el) for el in input().split(" ")])

def calc_prefix_sum(arr):
    new_arr = [0] * (len(arr) + 1)
    for i in range(1, len(new_arr)):
        new_arr[i] = new_arr[i - 1] + arr[i - 1]
    return new_arr

for i in range(num_rows):
    matrix[i] = calc_prefix_sum(matrix[i])

n_query = int(input())
for i in range(n_query):
    row1, col1, row2, col2 = map(int, input().split(" "))

    curr_sum = 0

    for row_idx in range(row1 - 1, row2):
        curr_sum += (matrix[row_idx][col2] - matrix[row_idx][col1 - 1])
    print(curr_sum)