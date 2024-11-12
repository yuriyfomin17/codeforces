n, num_operations = map(int, input().split(" "))
array = [int(el) for el in input().split(" ")]
class SegmentTree:
    def __init__(self):
        self.segment_tree_size = 2**n
        self.tree_arr = [0] * (self.segment_tree_size * 2)
        self.is_or = False

    def build_tree(self):
        def build_helper(l, h, i):
            if l >= len(array):
                return
            if h - l == 1:
                self.tree_arr[i] = array[l]
                self.is_or = True
                return

            mid = (l + h) // 2

            build_helper(l, mid, 2 * i + 1)
            build_helper(mid, h, 2 * i + 2)
            self.merge(i)
        build_helper(0, self.segment_tree_size, 0)
    def update(self, idx, v):
        def update_helper(l, h, i):
            if h - l == 1:
                self.tree_arr[i] = v
                self.is_or = True
                return
            mid = (l + h) // 2
            if idx < mid:
                update_helper(l, mid, 2 * i + 1)
            else:
                update_helper(mid, h, 2 * i + 2)
            self.merge(i)
        update_helper(0, self.segment_tree_size, 0)

    def merge(self, i):
        left = self.tree_arr[2 * i + 1]
        right = self.tree_arr[2 * i + 2]
        self.tree_arr[i] = left | right if self.is_or else left ^ right
        self.is_or = not self.is_or
    def find(self):
        return self.tree_arr[0]


tree = SegmentTree()
tree.build_tree()
for _ in range(num_operations):

    idx, v = map(int, input().split(" "))
    tree.update(idx - 1, v)
    print(tree.find())

