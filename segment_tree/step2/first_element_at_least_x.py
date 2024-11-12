array_size, number_of_operations = map(int, input().split(" "))
array = [int(el) for el in input().split(" ")]

class SegmentTree:
    def __init__(self):
        self.segmentation_tree_size = 1
        while self.segmentation_tree_size < array_size:
            self.segmentation_tree_size *= 2
        self.tree_arr = [-1] * (self.segmentation_tree_size * 2)

    def build(self):
        def build_helper(l, h, i):
            if l >= len(array):
                return
            if h - l == 1:
                self.tree_arr[i] = array[l]
                return
            mid = (l + h) // 2
            build_helper(l, mid, 2 * i + 1)
            build_helper(mid, h, 2 * i + 2)
            self.merge(i)
        build_helper(0, self.segmentation_tree_size, 0)

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
        update_helper(0, self.segmentation_tree_size, 0)
    def find(self, value):
        def find_helper(l, h, i):
            if l >= array_size:
                return -1
            if h - l == 1:

                return l if self.tree_arr[i] >= value else -1
            curr_value = self.tree_arr[i]
            if curr_value < value: return -1

            mid = (l + h) // 2
            res = find_helper(l, mid, 2 * i + 1)
            if res == -1:
                return find_helper(mid, h, 2 * i + 2)
            return res
        return find_helper(0, self.segmentation_tree_size, 0)

    def merge(self, i):
        self.tree_arr[i] = max(self.tree_arr[2 * i + 1], self.tree_arr[2 * i + 2])

tree = SegmentTree()
tree.build()
for _ in range(number_of_operations):
    input_text = input()
    if input_text.startswith("1"):
        _, i, v = map(int, input_text.split(" "))
        tree.update(i, v)
    else:
        _, x = map(int, input_text.split(" "))
        print(tree.find(x))
