array_size =  int(input())
array = [int(el) for el in input().split(" ")]

class SegmentationTree:
    def __init__(self):
        self.tree_size = 1
        self.inf = 10**6
        while self.tree_size < array_size:
            self.tree_size *= 2
        self.tree_arr = [0] * (self.tree_size * 2)

    def update(self, idx):
        def update_helper(lo, hi, i):
            if lo > idx: return

            if hi - lo == 1:
                self.tree_arr[i] = 1
                return

            mid = (lo + hi) // 2
            if idx < mid:
                update_helper(lo, mid, 2 * i + 1)
            else:
                update_helper(mid, hi, 2 * i + 2)
            self.tree_arr[i] = self.tree_arr[2 * i + 1] + self.tree_arr[2 * i + 2]
        update_helper(0, self.tree_size, 0)


    def find_sum(self, ql, qh):
        def find_sum_helper(lo, hi, i):
            if qh <= lo or ql >= hi:
                return 0
            if ql <= lo and hi <= qh:
                return self.tree_arr[i]

            mid = (lo + hi) // 2
            return find_sum_helper(lo, mid, 2 * i + 1) + find_sum_helper(mid, hi, 2 * i + 2)


        return find_sum_helper(0, self.tree_size, 0)

tree = SegmentationTree()

res = []
for idx, el in enumerate(array):

    res.append(str(tree.find_sum(el, array_size)))
    tree.update(el - 1)

print(" ".join(res))



