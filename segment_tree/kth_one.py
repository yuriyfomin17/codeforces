size_of_array, num_operations = map(int, input().split(" "))
array = [int(el) for el in input().split(" ")]

class SegmentTree:
    def __init__(self):
        self.segment_tree_size = 1

        while self.segment_tree_size < size_of_array:
            self.segment_tree_size *= 2
        self.segment_tree_arr = [(0, 0)] * (self.segment_tree_size * 2)

    def build_tree(self):
        def build_helper(l, h, i):
            if l >= len(array):
                return
            if h - l == 1:
                self.segment_tree_arr[i] = (l, array[l])
                return

            mid = (l + h) // 2
            build_helper(l, mid, 2 * i + 1)
            build_helper(mid, h, 2 * i + 2)
            self.merge(i)

        build_helper(0, self.segment_tree_size, 0)
    def update(self, idx):
        def update_helper(l, h, i):
            if h - l == 1:
                _, bit = self.segment_tree_arr[i]
                self.segment_tree_arr[i]  = (idx, bit ^ 1)
                return
            mid = (l + h) // 2
            if idx < mid:
                update_helper(l, mid, 2 * i + 1)
            else:
                update_helper(mid, h, 2 * i + 2)
            self.merge(i)
        update_helper(0, self.segment_tree_size, 0)
    def find(self, k):
        def find_helper(l, h, i, curr_k):

            if h - l == 1:
                return self.segment_tree_arr[i][0]
            mid = (l + h ) // 2
            _, left_one_sum = self.segment_tree_arr[2 * i + 1]
            if curr_k >= left_one_sum:
                return find_helper(mid, h, 2 * i + 2, curr_k - left_one_sum)
            return find_helper(l, mid, 2 * i + 1, curr_k)
        return find_helper(0, self.segment_tree_size, 0, k)

    def merge(self, i):
        _, left_sum = self.segment_tree_arr[2 * i + 1]
        _, right_sum = self.segment_tree_arr[2 * i + 2]
        self.segment_tree_arr[i] = (0, left_sum + right_sum)

tree = SegmentTree()
tree.build_tree()
for _ in range(num_operations):
    operation_type, x = map(int, input().split(" "))
    if operation_type == 1:
        tree.update(x)
    else:
        print(tree.find(x))

