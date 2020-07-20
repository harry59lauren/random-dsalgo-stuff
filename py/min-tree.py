from global_structures import BST, height, preorder, inorder

def min_tree(tree, arr, i, j):
    if i >= j:
        return
    mid = (i + j) // 2
    tree.insert(arr[mid])
    #print(str(arr[mid]) + ",")
    min_tree(tree, arr, i, mid)
    min_tree(tree, arr, mid + 1, j)



tree = BST()
arr = [i for i in range(1,16)]
min_tree(tree, arr, 0, len(arr))

print(inorder(tree.root))

#print(height(tree.root))