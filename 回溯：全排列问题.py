#数组中没有重复的元素
# def backtrack(
#         state: list[int], choices:list[int],selected:list[bool],res:list[list[int]]
# ):
#     if len(state) == len(choices):
#         res.append(list(state))
#         return
#     for i,choice in enumerate(choices):
#         if not selected[i]:
#             selected[i]=True
#             state.append(choice)
#             backtrack(state,choices,selected,res)
#             selected[i]=False
#             state.pop()
#
# def permutation_i(nums:list[int])->list[list[int]]:
#     res=[]
#     backtrack(state=[],choices=nums,selected=[False]*len(nums),res=res)
#     return res
#
# if __name__ == "__main__":
#     nums = [1,2,3]
#     res = permutation_i(nums)
#     print(f"输入数组nums={nums} , {res}")

#数组中有重复的元素
def backtrack(
        state: list[int], choices:list[int],selected:list[bool],res:list[list[int]]
):
    duplicated : set[int] = set()
    if len(state) == len(choices):
        res.append(list(state))
        return
    for i,choice in enumerate(choices):
        if not selected[i] and choice not in duplicated:
            duplicated.add(choice)
            selected[i]=True
            state.append(choice)
            backtrack(state,choices,selected,res)
            selected[i]=False
            state.pop()

def permutation_i(nums:list[int])->list[list[int]]:
    res=[]
    backtrack(state=[],choices=nums,selected=[False]*len(nums),res=res)
    return res

if __name__ == "__main__":
    nums = [1,1,2,3]
    res = permutation_i(nums)
    print(f"输入数组nums={nums} , {res}")
