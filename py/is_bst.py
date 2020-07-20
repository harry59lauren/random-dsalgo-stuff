from global_structures import TreeNode

def bst(t, upper, lower):
    pass

def is_lesser(t, upper):
    return t.value < upper and is_subtree_lesser(t.left, upper) and is_subtree_lesser(t.right, upper)

def is_subtree_greater(t, lower):
    return t.value > lower and is_subtree_greater(t.left, lower) and is_subtree_greater(t.right, lower)


def in_range(t, lower, upper):
    return lower < t < upper and \
           in_range(t.left , min(t.value, lower), max(t.value, upper)) and \
           in_range(t.right, min(t.value, lower), max(t.value, upper))