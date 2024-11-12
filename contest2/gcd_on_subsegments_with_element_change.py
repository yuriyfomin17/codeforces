array_size = int(input())
array = [int(el) for el in input().split(" ")]
num_operations = int(input())

class SegmentTree:
    def __init__(self):
        self.segment_array_size = 1
        while self.segment_array_size < array_size:
            self.segment_array_size *= 2
        self.tree_arr = [-1] * (self.segment_array_size * 2)

    def build_tree(self):
        def build_helper(l, h, i):
            if l >= array_size:
                return
            if h - l == 1:
                self.tree_arr[i] = array[l]
                return
            mid = (l + h) // 2
            build_helper(l, mid, 2 * i + 1)
            build_helper(mid, h, 2 * i + 2)
            self.merge(i)
        build_helper(0, self.segment_array_size, 0)

    def update(self, idx, value):
        def update_helper(l, h, i):
            if h - l == 1:
                self.tree_arr[i] = value
                return
            mid = (l + h) // 2
            if idx < mid:
                update_helper(l, mid, 2 * i + 1)
            else:
                update_helper(mid, h, 2 * i + 2)
            self.merge(i)
        update_helper(0, self.segment_array_size, 0)
    def find(self, ql, qh):
        def find_helper(lo, hi, i):
            if hi <= ql or lo >= qh:
                return -1

            if ql <= lo and hi <= qh:
                return self.tree_arr[i]
            if hi - lo == 1:
                return self.tree_arr[i]

            mid = (lo + hi) // 2
            left_value = find_helper(lo, mid, 2 * i + 1)
            right_value = find_helper(mid, hi, 2 * i + 2)
            if right_value == -1:
                return left_value
            if left_value == -1:
                return right_value
            return self.gcd(left_value, right_value) if ql != qh else left_value

        return find_helper(0, self.segment_array_size, 0)
    def merge(self, i):
        left_value = self.tree_arr[2 * i  + 1]
        right_value = self.tree_arr[2 * i + 2]
        if right_value == -1 or left_value == -1:
            self.tree_arr[i] = left_value if left_value != -1 else right_value
        else:
            self.tree_arr[i] = self.gcd(left_value, right_value)

    def gcd(self, a, b):
        def gcd_helper(max_num, min_num):
            if min_num == 0: return max_num
            return self.gcd(min_num, max_num % min_num)
        return gcd_helper(max(a, b), min(a, b))

tree = SegmentTree()
tree.build_tree()
res = []
for _ in range(num_operations):
    input_text = input()
    if input_text.startswith("s"):
        ql, qr = map(int, input_text[2:].split(" "))
        res.append(str(tree.find(ql - 1 , qr)))
    else:
        idx, value = map(int, input_text[2:].split(" "))
        str(tree.update(idx - 1, value))
print(" ".join(res))

