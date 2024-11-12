array_size, num_operations = map(int, input().split(" "))
array = [int(el) for el in input().split(" ")]


class MinCountSegmentTree:
    def __init__(self):
        self.segment_tree_size = 1

        while self.segment_tree_size < array_size:
            self.segment_tree_size *= 2

        self.tree_arr = [0] * (self.segment_tree_size * 2)

    def build_tree(self):
        def build_tree_helper(lo, hi, i):
            if lo >= len(array):
                return
            if hi - lo == 1:
                self.tree_arr[i] = (array[lo], 1)
                return
            mid = (lo + hi) // 2

            build_tree_helper(lo, mid, 2 * i + 1)
            build_tree_helper(mid, hi, 2 * i + 2)

            self.update_node(i)

        build_tree_helper(0, self.segment_tree_size, 0)

    def query(self, ql, qh):
        def query_helper(lo, hi, i):
            if qh <= lo or ql >= hi:
                return float('inf'), 1
            if ql <= lo and hi <= qh:
                return self.tree_arr[i]

            mid = (lo + hi) // 2

            left_min, left_count = query_helper(lo, mid, 2 * i + 1)
            right_min, right_count = query_helper(mid, hi, 2 * i + 2)
            if left_min < right_min:
                return left_min, left_count
            elif right_min < left_min:
                return right_min, right_count
            else:
                return left_min, left_count + right_count

        return query_helper(0, self.segment_tree_size, 0)


    def update(self, idx, value):
        def update_helper(lo, hi, i):
            if hi - lo == 1:
                self.tree_arr[i] = (value, 1)
                return
            mid = (lo + hi) // 2
            if idx < mid:
                update_helper(lo, mid, 2 * i + 1)
            else:
                update_helper(mid, hi, 2 * i + 2)

            self.update_node(i)
        update_helper(0, self.segment_tree_size, 0)

    def update_node(self, i):
        left_min, left_count = self.tree_arr[2 * i + 1] if self.tree_arr[2 * i + 1] != 0 else (float('inf'), 1)
        right_min, right_count = self.tree_arr[2 * i + 2] if self.tree_arr[2 * i + 2] != 0 else (float('inf'), 1)
        if left_min < right_min:
            self.tree_arr[i] = (left_min, left_count)
        elif right_min < left_min:
            self.tree_arr[i] = (right_min, right_count)
        else:
            self.tree_arr[i] = (left_min, left_count + right_count)

tree = MinCountSegmentTree()
tree.build_tree()
for _ in range(num_operations):
    operation_type, x, y = map(int, input().split(" "))
    if operation_type == 1:
        tree.update(x, y)
    else:
        min_num, ct = tree.query(x, y)
        print(min_num, ct)
