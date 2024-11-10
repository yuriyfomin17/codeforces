no_of_elements, no_of_queries = map(int, input().split())
array = [int(el) for el in input().split(" ")]


num_of_repeated_elements = [0] * (no_of_elements + 1)

for _ in range(no_of_queries):
    l, r  = map(int, input().split())
    num_of_repeated_elements[l - 1] += 1
    num_of_repeated_elements[r] -= 1


for i in range(1, len( num_of_repeated_elements)):
    num_of_repeated_elements[i] += num_of_repeated_elements[i - 1]

array.sort(reverse=True)
num_of_repeated_elements.sort(reverse=True)

print(sum(el * num_of_repeated_elements[idx] for idx, el in enumerate(array)))