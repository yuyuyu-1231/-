# class TreeNode:
#     def __init__(self,val: int = 0):
#         self.val: int = val
#         self.left: TreeNode | None = None
#         self.right: TreeNode | None = None
#
# def dfs(
#         preorder: list[int],
#         inorder_map: dict[int,int],
#         i:int,
#         l:int,
#         r:int,
# )-> TreeNode | None:
#     if r-l <0:
#         return None
#     root = TreeNode(preorder[i])
#     m = inorder_map[preorder[i]]
#     root.left = dfs(preorder,inorder_map,i+1,l,m-1)
#     root.right = dfs(preorder,inorder_map,i+m-l+1,m+1,r)
#     return root
#
# def build_tree(preorder:list[int],inorder:list[int]) -> TreeNode | None:
#     inorder_map = {val:i for i,val in enumerate(inorder)}
#     root = dfs(preorder,inorder_map,0,0,len(preorder)-1)
#     return root
# if __name__ == '__main__':
#     preorder = [1,2,4,5,3,6,7]
#     inorder = [4,2,5,1,6,3,7]
#     root = build_tree(preorder,inorder)

class TreeNode:
    def __init__(self,val: int = 0):
        self.val : int =val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

def dfs(
        preorder: list[int],
        inorder_map: dict[int,int],
        i:int,
        l:int,
        r:int,
)-> TreeNode | None:
    if r-l <0:
        return None
    root = TreeNode(preorder[i])
    m = inorder_map[preorder[i]]
    root.left = dfs(preorder,inorder_map,i+1,l,m-1)
    root.right = dfs(preorder,inorder_map,i+1+m-l,m+1,r)
    return root

def build_tree(preorder:list[int],inorder:list[int])-> TreeNode | None:
    inorder_map = {val:i for i,val in enumerate(inorder)}
    root = dfs(preorder,inorder_map,0,0,len(preorder)-1)
    return root

if __name__ == '__main__':
    preorder = [1,2,4,5,3,6,7]
    inorder = [4,2,5,1,6,3,7]
    root = build_tree(preorder,inorder)