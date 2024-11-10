import collections

n_query = 7

def binary_tree_to_string(tree):
    result = ''
    nodes = collections.deque()
    visited = set()
    first = True
    null_nodes_pending = 0

    result += '['
    nodes.append(tree)

    while nodes:
        node = nodes.popleft()
        if id(node) in visited:
            raise RuntimeError('Detected a cycle in the tree')
        if node:
            if first:
                first = False
            else:
                result += ', '

            while null_nodes_pending:
                result += 'null, '
                null_nodes_pending -= 1

            result += '"{}"'.format(node.data)

            visited.add(id(node))
            nodes.append(node.left)
            nodes.append(node.right)
        else:
            null_nodes_pending += 1

    result += ']'
    return result
def equal_binary_trees(tree1, tree2):
    s = [(tree1, tree2)]

    while s:
        node1, node2 = s.pop()

        if (node1 is None) != (node2 is None):
            return False

        if node1:
            if node1.data != node2.data:
                return False
            s.append((node1.left, node2.left))
            s.append((node1.right, node2.right))

    return True
class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def __repr__(self):
        return str(binary_tree_to_string(self))

    def __str__(self):
        return self.__repr__()
    def __eq__(self, other):
        return equal_binary_trees(self, other)


def build_tree(l, h):
    if l == h:
        return Node(l)
    if l > h:
        return None

    mid = l + (h - l) // 2
    left_subtree = build_tree(l, mid - 1)
    right_subtree = build_tree(mid + 1, h)
    return Node(mid, left_subtree, right_subtree)

tree = build_tree(0, 16)
print(tree)
