import collections

class ListNode:

    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f'ListNode({self.value}, {self.next})'


class TreeNode:

    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def is_leaf(self):
        return not self.right and not self.left

    def __repr__(self):
        return f'TreeNode(id={id(self)}, value={self.value})'

class BST :

    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value, None, None)
        else:
            cur = self.root
            while True:
                if value > cur.value:
                    if not cur.right:
                        cur.right = TreeNode(value, None, None)
                        return
                    cur = cur.right
                else:
                    if not cur.left:
                        cur.left = TreeNode(value, None, None)
                        return
                    cur = cur.left

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, root):
        if not root:
             return []
        return self._inorder(root.left) +  self._inorder(root.right) + [root]

def height(root):
    return 0 if not root or root.is_leaf() else 1 + max(height(root.left), height(root.right))

def preorder(root):
    queue = collections.deque([root])
    history = {}
    po = []

    while queue:
        node = queue[-1]
        idn  = id(node)

        if idn not in history.keys():
            history[id(node)] = [False, False]

        if node.left and not history[idn][0]:
            queue.append(node.left)
            history[idn][0] = True
            continue

        if node.right and not history[idn][1]:
            queue.append(node.right)
            history[idn][1] = True
            continue

        po.append(queue.pop().value)

    return po


def inorder(root):
    stack = collections.deque([])
    traversal = []
    cur = root

    while True :
        if not cur:
            top = stack.pop()
            traversal.append(top.value)
            cur = top.right
        else:
            stack.append(cur)
            cur = cur.left

        if not stack and not cur:
            break
        
    return traversal
        
            

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = collections.deque([root])
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        

