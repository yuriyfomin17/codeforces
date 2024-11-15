
array_size, number_of_operations = map(int, input().split(" "))
array = [int(el) for el in input().split(" ")]

class SegmentationTree:
    def __init__(self):
        self.segmentation_tree_size = 1
        self.tree_inf = -1
        while self.segmentation_tree_size < array_size:
            self.segmentation_tree_size *= 2
        self.tree_arr = [self.tree_inf] * (self.segmentation_tree_size * 2)

    def build(self):
        def build_helper(lo, hi, i):
            if lo >= array_size:
                return
            if hi - lo == 1:
                self.tree_arr[i] = array[lo]
                return
            mid = (lo + hi) // 2
            build_helper(lo, mid, 2 * i + 1)
            build_helper(mid, hi, 2 * i + 2)
            self.merge(i)
        build_helper(0, self.segmentation_tree_size, 0)

    def update(self, idx, value):
        def update_helper(lo, hi, i):
            if hi - lo == 1:
                self.tree_arr[i] = value
                return
            mid = (lo + hi) // 2

            if idx < mid:
                update_helper(lo, mid, 2 * i + 1)
            else:
                update_helper(mid, hi, 2 * i + 2)
            self.merge(i)
        update_helper(0, self.segmentation_tree_size, 0)
    def find(self, lower_bound, value):
        def find_helper(lo, hi, i):
            if hi <= lower_bound: return -1
            if hi - lo == 1:
                return lo if lo >= lower_bound and self.tree_arr[i] >= value else -1

            mid = (lo + hi) // 2
            curr_value = self.tree_arr[i]
            if curr_value < value:
                return -1

            res = find_helper(lo, mid, 2 * i + 1)
            if res == -1:
                return find_helper(mid, hi, 2 * i + 2)
            return res
        return find_helper(0, self.segmentation_tree_size, 0)

    def merge(self, i):
        self.tree_arr[i] = max(self.tree_arr[2 * i + 1], self.tree_arr[2 * i + 2])

tree = SegmentationTree()
tree.build()
# print(tree.tree_arr)
for _ in range(number_of_operations):
    operation_type, i, x = map(int, input().split(" "))
    if operation_type == 0:
        tree.update(i - 1, x)
    else:
        idx = tree.find(i - 1, x)
        print(idx + 1 if idx != -1 else -1)
