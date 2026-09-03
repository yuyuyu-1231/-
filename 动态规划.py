# #暴力搜索
# def dfs(i: int) -> int:
#     if i == 1 or i ==2:
#         return i
#     count = dfs(i-1) + dfs(i-2)
#     return count
#
# def climbing_stairs_dfs(n: int) -> int:
#     return dfs(n)
#
# if __name__ == '__main__':
#     n=9
#     res = climbing_stairs_dfs(n)
#     print(res)


# def dfs(i:int,mem:list[int]) -> int:
#     if i==1 or i==2:
#         return i
#     if mem[i] != -1:
#         return mem[i]
#     count = dfs(i-1,mem) + dfs(i-2,mem)
#     mem[i] = count
#     return count
#
# def climbing_stairs_dfs_mem(n: int) -> int:
#     mem = [-1] * (n + 1)
#     return dfs(n,mem)
#
# if __name__ == "__main__":
#     n = 9
#     res =   climbing_stairs_dfs_mem(n)
#     print(res)
#


# def climbing_stairs_dp(n:int) ->int :
#     if n == 1 or n==2:
#         return n
#     dp = [0]*(n+1)
#     dp[1],dp[2]=1,2
#     for i in range(3,n+1):
#         dp[i] = dp[i-1]+dp[i-2]
#     return dp[n]
# if __name__ == '__main__':
#     n = 9
#     res = climbing_stairs_dp(n)
#     print(res)


# def climbing_stairs_dp_ciomp(n:int) -> int:
#     if n==1 or n==2:
#         return n
#     a,b = 1,2
#     for _ in range(3,n+1):
#         a,b =b,a+b
#     return b
#
# if __name__ == "__main__":
#     n=9
#     res = climbing_stairs_dp_ciomp(n)
#     print(res)

# def min_cost_climbing_stairs_dp(cost: list[int]) -> int:
#     n = len(cost) - 1
#     if n == 1 or n == 2:
#         return cost[n]
#     dp = [0]* (n+1)
#     dp[1],dp[2]=cost[1],cost[2]
#     for i in range(3,n+1):
#         dp[i] = min(dp[i-1],dp[i-2]) + cost[i]
#     return dp[n]
#
# if __name__ == '__main__':
#     cost = [0, 1, 10, 1, 1, 1, 10, 1, 1, 10, 1]
#     print(f"输入楼梯的代价列表为 {cost}")
#     res = min_cost_climbing_stairs_dp(cost)
#     print(f"爬完楼梯的最低代价为 {res}")

def climbing_stairs_constraint_dp(n: int) -> int:
    if n ==1 or n==2:
        return 1
    dp = [[0] * 3 for _ in range(n + 1)]
    dp[1][1], dp[1][2] = 1, 0
    dp[2][1], dp[2][2] = 0, 1
    for i in range(3, n + 1):
        dp[i][1] = dp[i - 1][2]
        dp[i][2] = dp[i - 1][1] + dp[i - 1][2]
    return dp[n][1] + dp[n][2]

if __name__ == '__main__':
    n = 9
    res = climbing_stairs_constraint_dp(n)
    print(res)
