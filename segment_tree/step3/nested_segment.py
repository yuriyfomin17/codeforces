n = int(input())
array = [int(el) for el in input().split(" ")]

class SegmentTree:
    def __init__(self):
        self.segment_tree_size = 1
        while self.segment_tree_size < len(array):
            self.segment_tree_size *= 2

        self.tree_arr = [0] * (self.segment_tree_size * 2)


    def update(self, idx):
        def update_helper(lo, hi, i):
            if hi - lo == 1:
                self.tree_arr[i] = 1
                return
            mid = (lo + hi) // 2

            if idx < mid:
                update_helper(lo, mid, 2 * i + 1)
            else:
                update_helper(mid, hi, 2 * i + 2)
            self.tree_arr[i] = self.tree_arr[2 * i + 1] + self.tree_arr[2 * i + 2]
        update_helper(0, self.segment_tree_size, 0)

    def find_sum(self, ql, qh):
        def find_sum_helper(lo, hi, i):
            if lo >= qh or hi <= ql: return 0
            if ql  <= lo and hi <= qh:
                return self.tree_arr[i]
            mid = (lo + hi) // 2
            return find_sum_helper(lo, mid, 2 * i + 1) + find_sum_helper(mid, hi, 2 * i + 2)
        return find_sum_helper(0, self.segment_tree_size, 0)

tree = SegmentTree()
visited_num = [0] * n
res = [0] * n

for idx, el in enumerate(array):
    if visited_num[el - 1] != 0:
        res[el - 1] = tree.find_sum(visited_num[el - 1] - 1 , idx + 1)
        tree.update(visited_num[el - 1] - 1 )
    else:
        visited_num[el - 1] = (idx + 1)

print(" ".join(str(el) for el in res))