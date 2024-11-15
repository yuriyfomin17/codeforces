array_size = int(input())
array = [int(el) for el in input().split(" ")]


class SegmentationTree:

    def __init__(self):
        self.segmentation_tree_size = 1
        while self.segmentation_tree_size < array_size:
            self.segmentation_tree_size *= 2
        self.tree_arr = [0] * (self.segmentation_tree_size * 2)

    def build_tree(self):
        def build_tree_helper(lo, hi, i):
            if lo >= array_size:
                return
            if hi - lo == 1:
                self.tree_arr[i] = 1
                return

            mid = (lo + hi) // 2
            build_tree_helper(lo, mid, 2 * i + 1)
            build_tree_helper(mid, hi, 2 * i + 2)
            self.tree_arr[i] = self.tree_arr[2 * i + 1] + self.tree_arr[2 * i + 2]

        build_tree_helper(0, self.segmentation_tree_size, 0)

    def find_idx(self, num_to_left):
        def find_idx_helper(lo, hi, i, curr_num_to_left):
            if hi - lo == 1:
                self.tree_arr[i] -= 1
                return lo

            mid = (lo + hi) // 2
            numbers_to_left = self.tree_arr[2 * i + 1]

            if numbers_to_left >= curr_num_to_left:
                ans = find_idx_helper(lo, mid, 2 * i + 1, curr_num_to_left)
                self.tree_arr[i] -= 1
                return ans
            ans = find_idx_helper(mid, hi, 2 * i + 2, curr_num_to_left - numbers_to_left)
            self.tree_arr[i] -= 1
            return ans

        return find_idx_helper(0, self.segmentation_tree_size, 0, num_to_left)


tree = SegmentationTree()
tree.build_tree()
res = [""] * array_size
for idx in reversed(range(len(array))):
    num_to_left = array[idx]
    res[idx] = str(1 + tree.find_idx(idx + 1 - num_to_left))
    array_size -= 1

print(" ".join(res))
