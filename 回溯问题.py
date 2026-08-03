# class TreeNode:
#     def __init__(self,val:int=0):
#         self.val:int =val
#         self.left:TreeNode | None = None
#         self.right:TreeNode | None = None
#
# def list_to_tree_dfs(arr:list, i : int)-> TreeNode | None:
#     if i<0 or i>=len(arr) or arr[i] is None:
#         return None
#     root = TreeNode(arr[i])
#     root.left = list_to_tree_dfs(arr, 2 * i + 1)
#     root.right = list_to_tree_dfs(arr,2 * i + 2)
#     return root
#
# def list_to_tree(arr:list):
#     return list_to_tree_dfs(arr,0)
#
# def pre_order(root:TreeNode,res):
#     if root is None:
#         return
#     if root.val == 7:
#         res.append(root)
#     pre_order(root.left, res)
#     pre_order(root.right, res)
#
# if __name__ == "__main__":
#     root = list_to_tree([1,7,3,4,5,6,7])
#     res = list[TreeNode]()
#     pre_order(root,res)
#     print([node.val for node in res])
#     print(res)


# class TreeNode:
#     def __init__(self,val: int =0):
#         self.val : int = val
#         self.left: TreeNode | None = None
#         self.right: TreeNode | None = None
#
# def list_to_tree_dfs(arr:list[int], i:int) -> TreeNode | None:
#     if i<0 or i>=len(arr) or arr[i] is None:
#         return None
#     root = TreeNode(arr[i])
#     root.left = list_to_tree_dfs(arr,2*i+1)
#     root.right = list_to_tree_dfs(arr,2*i+2)
#     return root
# def list_to_tree(arr:list[int]):
#     return list_to_tree_dfs(arr,0)
#
# def pre_order(root:TreeNode):
#     if root is None:
#         return
#     path.append(root)
#     if root.val == 7:
#         res.append(list(path))
#     pre_order(root.left)
#     pre_order(root.right)
#     path.pop()
#
# if __name__ == "__main__":
#     root = list_to_tree([1,7,3,4,5,6,7])
#     path : list[TreeNode] = []
#     res : list[list[TreeNode]] = []
#     pre_order(root)
#     print("\n输出所有根节点到节点7的路径")
#     for path in res:
#         print([node.val for node in path])

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

def is_solution(state:list[TreeNode])-> bool:
    return state and state[-1]==7

def record_solution(state:list[TreeNode],res:list[list[TreeNode]]) -> None:
    res.append(list(state))

def is_valid(state: list[TreeNode], choice: TreeNode) -> bool:
    return choice is not None and choice.val != 3

def make_choice(state:list[TreeNode],choice:TreeNode):
    state.append(choice)

def undo_choice(state:list[TreeNode],choice:TreeNode):
    state.pop()

def backtrack(
        state:list[TreeNode],
        choices:list[TreeNode],
        res:list[list[TreeNode]]
):
    if is_solution(state):
        record_solution(state,res)
    for choice in choices:
        if is_valid(state, choice):
            make_choice(state, choice)
            backtrack(state, [choice.left, choice.right], res)
            undo_choice(state, choice)

if __name__ == "__main__":
    root = list_to_tree([1, 7, 3, 4, 5, 6, 7])

    # 回溯算法
    res = []
    backtrack(state=[], choices=[root], res=res)
    print("\n输出所有路径")
    for path in res:
        print([node.val for node in path])