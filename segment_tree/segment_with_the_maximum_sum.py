array_size, num_operations = map(int, input().split(" "))
array = [int(el) for el in input().split(" ")]


class SegmentationTree:
    def __init__(self):
        self.negative_inf = 0
        self.non_node = (0, 0, 0, 0)
        self.segmentation_tree_size = 1
        while self.segmentation_tree_size < array_size:
            self.segmentation_tree_size *= 2
        self.tree_arr = [self.negative_inf] * (self.segmentation_tree_size * 2)

    def build_tree(self):
        def build_tree_helper(l, h, i):
            if l >= len(array):
                return
            if h - l == 1:
                self.tree_arr[i] = (array[l], array[l], array[l], array[l])
                return
            mid = (l + h) // 2
            build_tree_helper(l, mid, 2 * i + 1)
            build_tree_helper(mid, h, 2 * i + 2)

            left_prefix, left_sum, left_suffix, left_seg = self.tree_arr[2 * i + 1] if self.tree_arr[2 * i + 1] != self.negative_inf else self.non_node
            right_prefix, right_sum, right_suffix, right_seg = self.tree_arr[2 * i + 2] if self.tree_arr[2 * i + 2] != self.negative_inf else self.non_node

            max_prefix = max(left_prefix, left_sum + right_prefix)
            next_sum = left_sum + right_sum
            max_suffix = max(right_suffix, right_sum + left_suffix)
            next_seg = max(left_seg, right_seg, left_suffix
                           + right_prefix)
            self.tree_arr[i] = (max_prefix, next_sum, max_suffix, next_seg)

        build_tree_helper(0, self.segmentation_tree_size, 0)

    def update(self, idx, value):
        def update_helper(l, h, i):
            if h - l == 1:
                self.tree_arr[i] = (value, value, value, value)
                return
            mid = (l + h) // 2
            if idx < mid:
                update_helper(l, mid, 2 * i + 1)
            else:
                update_helper(mid, h, 2 * i + 2)

            left_prefix, left_sum, left_suffix, left_seg = self.tree_arr[2 * i + 1] if self.tree_arr[
                                                                                           2 * i + 1] != self.negative_inf else self.non_node
            right_prefix, right_sum, right_suffix, right_seg = self.tree_arr[2 * i + 2] if self.tree_arr[
                                                                                               2 * i + 2] != self.negative_inf else self.non_node

            max_prefix = max(left_prefix, left_sum + right_prefix)
            next_sum = left_sum + right_sum
            max_suffix = max(right_suffix, right_sum + left_suffix)
            next_seg = max(left_seg, right_seg, left_suffix
                           + right_prefix)
            self.tree_arr[i] = (max_prefix, next_sum, max_suffix, next_seg)

        update_helper(0, self.segmentation_tree_size, 0)

    def maximum_sum(self):
        prefix, total_sum, suffix, seg = self.tree_arr[0]
        return max(seg,0)


segmentation_tree = SegmentationTree()
segmentation_tree.build_tree()
print(segmentation_tree.maximum_sum())
for _ in range(num_operations):
    i, v = map(int, input().split(" "))
    segmentation_tree.update(i, v)
    print(segmentation_tree.maximum_sum())
