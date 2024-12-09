class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, root_val, val, op='+'):
    if root is None:
        if op == '+':
            return Node(val+root_val)
        else:
            return Node(val*root_val)

    root.left = insert(root.left, root.val, val, '+')
    root.right = insert(root.right, root.val, val,'*')

    return root

def search_dfs(root, target):
    if not root:
        return False

    if root.val == target:
        return True

    return search_dfs(root.left, target) or search_dfs(root.right, target)

ans = 0
with open('input', 'r') as f:
    for line in f:
        tokens = line.split(':')
        target = int(tokens[0])
        nums = [int(n) for n in tokens[1].strip().split()]

        root = Node(nums[0])
        for i in nums[1:]:
            root = insert(root, root.val, i)

        if search_dfs(root, target):
            ans += target

print(ans)
