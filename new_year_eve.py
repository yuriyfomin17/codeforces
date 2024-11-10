from time import perf_counter

first_line = input()

n = ""
idx = 0
while idx < len(first_line) and first_line[idx] != " ":
    n += first_line[idx]
    idx += 1
idx += 1
n = int(n)
k = ""
while idx < len(first_line) and first_line[idx] != " ":
    k += first_line[idx]
    idx += 1

k = int(k)
if k == 1:
    print(n)
else:
    max_number = n
    curr_number = n
    ct = 0
    needed_number = 0
    while curr_number:
        if curr_number & 1 == 0 :
            needed_number |= (1 << ct)

        curr_number >>= 1
        ct += 1

    print(n ^ needed_number)