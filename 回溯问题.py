class TreeNode:
    def __init__(self,val:int=0):
        self.val:int =val
        self.left:TreeNode | None = None
        self.right:TreeNode | None = None

def list_to_tree_dfs(arr:list, i : int)-> TreeNode | None:
    if i<0 or i>=len(arr) or arr[i] is None:
        return None
    root = TreeNode(arr[i])
    root.left = list_to_tree_dfs(arr, 2 * i + 1)
    root.right = list_to_tree_dfs(arr,2 * i + 2)
    return root

def list_to_tree(arr:list):
    return list_to_tree_dfs(arr,0)

def pre_order(root:TreeNode,res):
    if root is None:
        return
    if root.val == 7:
        res.append(root)
    pre_order(root.left, res)
    pre_order(root.right, res)

if __name__ == "__main__":
    root = list_to_tree([1,7,3,4,5,6,7])
    res = list[TreeNode]()
    pre_order(root,res)
    print([node.val for node in res])
    print(res)