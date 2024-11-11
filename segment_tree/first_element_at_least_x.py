array_size, num_operations = map(int, input().split(" "))
array = [int(el) for el in input().split(" ")]


class SegmentTree:
    def __init__(self):
        self.segment_tree_size = 1
        while self.segment_tree_size < array_size:
            self.segment_tree_size *= 2
        self.tree_arr = [-1] * (self.segment_tree_size * 2)

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

        build_helper(0, self.segment_tree_size, 0)

    def update(self, idx, value):
        def update_helper(l, h, i):
            if h - l == 1:
                self.tree_arr[i] =  value
                return
            mid = (l + h) // 2
            if idx < mid:
                update_helper(l, mid, 2 * i + 1)
            else:
                update_helper(mid, h, 2 * i + 2)
            self.merge(i)

        update_helper(0, self.segment_tree_size, 0)

    def find(self, value):
        def find_helper(l, h, i):
            if self.tree_arr[i] < value:
                return -1
            if h - l == 1: return l


            mid = (l + h) // 2
            res = find_helper(l, mid, 2 * i + 1, )
            if res == -1:
                return find_helper(mid, h, 2 * i + 2)
            return res


        return find_helper(0, self.segment_tree_size, 0)

    def merge(self, i):
        left_max_value = self.tree_arr[2 * i + 1]
        right_max_value = self.tree_arr[2 * i + 2]

        self.tree_arr[i] = max(left_max_value, right_max_value)


segment_tree = SegmentTree()
segment_tree.build()

for _ in range(num_operations):
    curr_input = input()
    if curr_input.startswith("1"):
        operation_type, i, v = map(int, curr_input.split(" "))
        segment_tree.update(i, v)
    else:
        operation_type, v = map(int, curr_input.split(" "))
        print(segment_tree.find(v))
