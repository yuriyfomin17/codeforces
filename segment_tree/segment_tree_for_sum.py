
array_size, number_of_query = map(int, input().split(" "))
array = [int(el) for el in input().split(" ")]



class SegmentationTree:
    def __init__(self, ):
        self.segmentation_tree_array_size = 1
        while self.segmentation_tree_array_size < array_size:
            self.segmentation_tree_array_size *= 2
        self.tree_arr = [0] * (self.segmentation_tree_array_size * 2)
    def build_tree(self):
        def build_tree_helper(lo, hi, i):
            if lo >= len(array): return
            if hi - lo == 1:
                self.tree_arr[i] = array[lo]
                return
            mid = (lo + hi) // 2
            build_tree_helper(lo, mid, 2 * i + 1)
            build_tree_helper(mid, hi, 2 * i + 2)
            self.tree_arr[i] = self.tree_arr[2 * i + 1] + self.tree_arr[2 * i + 2]
        build_tree_helper(0, self.segmentation_tree_array_size, 0)
    def update_tree(self, idx, value):
        def update_tree_helper(lo, hi, i):
            if hi - lo == 1:
                self.tree_arr[i] = value
                return
            mid = (lo + hi ) // 2
            if idx < mid:
                update_tree_helper(lo, mid, 2 * i + 1)
            else:
                update_tree_helper(mid, hi, 2 * i + 2)
            self.tree_arr[i] = self.tree_arr[2 * i + 1] + self.tree_arr[2 * i + 2]
        update_tree_helper(0, self.segmentation_tree_array_size, 0)

    def query_tree(self, ql, qh):
        def query_tree_helper(lo, hi, i):
            if hi <= ql or lo >= qh:
                return 0
            if ql <= lo and hi <= qh:
                return self.tree_arr[i]
            mid = (lo + hi) // 2
            return query_tree_helper(lo, mid, 2 * i + 1) + query_tree_helper(mid, hi, 2 * i + 2)
        return query_tree_helper(0, self.segmentation_tree_array_size, 0)




segmentation_tree = SegmentationTree()
segmentation_tree.build_tree()

for _ in range(number_of_query):
    operation_type, x, y = map(int, input().split(" "))

    if operation_type == 1:
        segmentation_tree.update_tree(x, y)
    else:
        print(segmentation_tree.query_tree(x, y))