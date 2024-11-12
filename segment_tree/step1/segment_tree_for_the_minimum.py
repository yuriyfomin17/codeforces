
size_of_array, num_operations = map(int, input().split(" "))
array = [int(el) for el in input().split(" ")]

class MinSegmentTree:
    def __init__(self):
        self.segmenet_tree_size = 1
        while self.segmenet_tree_size < size_of_array:
            self.segmenet_tree_size *= 2
        self.tree_arr = [0] * (self.segmenet_tree_size * 2)

    def build_tree(self):
        def build_tree_helper(lo, hi, i):
            if lo >= len(array): return
            if hi - lo == 1:
                self.tree_arr[i] = array[lo]
                return

            mid = (lo + hi) // 2
            build_tree_helper(lo, mid, 2 * i + 1)
            build_tree_helper(mid, hi, 2 * i + 2)

            self.tree_arr[i] = min(self.tree_arr[2 * i + 1], self.tree_arr[2 * i + 2])
        build_tree_helper(0, self.segmenet_tree_size, 0)

    def update(self, idx, v):
        def update_helper(lo, hi, i):
            if hi - lo == 1:
                self.tree_arr[i] = v
                return
            mid = (lo + hi ) / 2

            if idx < mid:
                update_helper(lo, mid, 2 * i + 1)
            else:
                update_helper(mid, hi, 2 * i + 2)
            self.tree_arr[i] = min(self.tree_arr[2 * i + 1], self.tree_arr[2 * i + 2])
        update_helper(0, self.segmenet_tree_size, 0)

    def query(self, ql, qh):
        def query_helper(lo, hi, i):
            if hi <= ql or lo >= qh:
                return float('inf')
            if ql <= lo and hi <= qh:
                return self.tree_arr[i]
            mid = (lo + hi) // 2

            return min(
                query_helper(lo, mid, 2 * i + 1),
                query_helper(mid, hi, 2 * i + 2)
            )
        return query_helper(0, self.segmenet_tree_size, 0)

tree = MinSegmentTree()
tree.build_tree()
for _ in range(num_operations):
    operation_type, x, y = map(int, input().split(" "))
    if operation_type == 1:
        tree.update(x, y)
    else:
        print(tree.query(x, y))
