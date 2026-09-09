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

# def climbing_stairs_constraint_dp(n: int) -> int:
#     if n ==1 or n==2:
#         return 1
#     dp = [[0] * 3 for _ in range(n + 1)]
#     dp[1][1], dp[1][2] = 1, 0
#     dp[2][1], dp[2][2] = 0, 1
#     for i in range(3, n + 1):
#         dp[i][1] = dp[i - 1][2]
#         dp[i][2] = dp[i - 1][1] + dp[i - 1][2]
#     return dp[n][1] + dp[n][2]
#
# if __name__ == '__main__':
#     n = 9
#     res = climbing_stairs_constraint_dp(n)
#     print(res)

#暴力搜索
from math import inf

# def min_path_sum_dfs(grid:list[list[int]],i:int,j:int) -> int:
#     if i ==0 and j==0:
#         return grid[0][0]
#     if i<0 or j<0:
#         return inf
#     up = min_path_sum_dfs(grid,i-1,j)
#     left = min_path_sum_dfs(grid,i,j-1)
#     return min(up,left) + grid[i][j]
#
# if __name__ == "__main__":
#     grid = [[1, 3, 1, 5], [2, 2, 4, 2], [5, 3, 2, 1], [4, 3, 5, 2]]
#     n,m = len(grid),len(grid[0])
#     res = min_path_sum_dfs(grid, n - 1, m - 1)
#     print(res)

#记忆化搜索
# from math import inf
#
# def min_path_sum_dfs(grid:list[list[int]],mem:list[list[int]],i:int,j:int) -> int:
#     if i ==0 and j==0:
#         return grid[0][0]
#     if i<0 or j<0:
#         return inf
#     if mem[i][j] != -1:
#         return mem[i][j]
#     up = min_path_sum_dfs(grid,mem,i-1,j)
#     left = min_path_sum_dfs(grid,mem,i,j-1)
#     mem[i][j] = min(up,left) + grid[i][j]
#     return mem[i][j]
#
# if __name__ == "__main__":
#     grid = [[1, 3, 1, 5], [2, 2, 4, 2], [5, 3, 2, 1], [4, 3, 5, 2]]
#     n,m = len(grid),len(grid[0])
#     mem = [[-1]*m for _ in range(n)]
#     res = min_path_sum_dfs(grid,mem, n - 1, m - 1)
#
#     print(res)

#动态规划
# def min_path_sum_dp(grid:list[list[int]]) -> int:
#     n,m = len(grid),len(grid[0])
#     dp = [[0]*m for _ in range(n)]
#     dp[0][0] = grid[0][0]
#     for i in range(1,n):
#         dp[i][0] = dp[i-1][0] + grid[i][0]
#     for j in range(1,m):
#         dp[0][j] = dp[0][j-1] + grid[0][j]
#     for i in range(1,n):
#         for j in range(1,m):
#             dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
#     return dp[n-1][m-1]
#
# if __name__ == "__main__":
#     grid = [[1, 3, 1, 5], [2, 2, 4, 2], [5, 3, 2, 1], [4, 3, 5, 2]]
#     print(min_path_sum_dp(grid))
#
# #0-1背包问题
# def knapsack_dfs(wgt: list[int], val: list[int], i:int, c:int) -> int:
#     if i==0 or c==0:
#         return 0
#     if wgt[i-1] > c:
#         return knapsack_dfs(wgt,val,i-1,c)
#     no = knapsack_dfs(wgt,val,i-1,c)
#     yes = knapsack_dfs(wgt,val,i-1,c-wgt[i-1]) + val[i-1]
#     return max(no,yes)
#
# if __name__ == "__main__":
#     wgt = [10, 20, 30, 40, 50]
#     val = [50, 120, 150, 210, 240]
#     cap = 50
#     n = len(wgt)
#     res = knapsack_dfs(wgt,val,n,cap)
#     print(res)
#

#记忆化搜索
# def knapsack_dfs_mem(
#         wgt: list[int],val : list[int],mem:list[list[int]],i:int,c:int
# ) -> int:
#     if i==0 or c==0:
#         return 0
#     if wgt[i-1] > c:
#         return knapsack_dfs_mem(wgt,val,mem,i-1,c)
#     if mem[i][c] != -1:
#         return mem[i][c]
#     no = knapsack_dfs_mem(wgt,val,mem,i-1,c)
#     yes = knapsack_dfs_mem(wgt,val,mem,i-1,c-wgt[i-1]) + val[i-1]
#     mem[i][c] = max(no,yes)
#     return mem[i][c]
# if __name__ == "__main__":
#
#     wgt = [10, 20, 30, 40, 50]
#     val = [50, 120, 150, 210, 240]
#     cap = 50
#     n = len(wgt)
#     mem = [[-1]* (cap + 1) for _ in range(n + 1)]
#     res = knapsack_dfs_mem(wgt,val,mem,n,cap)
#     print(res)

#动态规划
# def knapsack_dp(wgt: list[int], val: list[int], n:int, c:int) -> int:
#     dp = [[0] * (c + 1) for _ in range(n + 1)]
#     for i in range(1, n + 1):
#         for j in range(1, c + 1):
#             if wgt[i - 1] > j:
#                 dp[i][j] = dp[i - 1][j]
#             else:
#                 dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wgt[i - 1]] + val[i - 1])
#     return dp[n][c]
#
# if __name__ == "__main__":
#     wgt = [10, 20, 30, 40, 50]
#     val = [50, 120, 150, 210, 240]
#     cap = 50
#     n = len(wgt)
#     res = knapsack_dp(wgt,val,n,cap)
#     print(res)
#

#空间优化
# def knapsack_dp_comp(wgt: list[int], val: list[int], cap: int) -> int:
#     n = len(wgt)
#     dp = [0] * (cap + 1)
#     for i in range(1, n + 1):
#         for j in range(cap, wgt[i - 1] - 1, -1):
#             if wgt[i-1] > j  :
#                 dp[j] = dp[j]
#             else:
#                 dp[j] = max(dp[j], dp[j - wgt[i - 1]] + val[i - 1])
#     return dp[cap]
#
# if __name__ == '__main__':
#     wgt = [10, 20, 30, 40, 50]
#     val = [50, 120, 150, 210, 240]
#     cap = 50
#     res = knapsack_dp_comp(wgt,val,cap)
#     print(res)

#零钱兑换问题
# def coin_change_dp(coins: list[int], amt: int) -> int:
#     n = len(coins)
#     MAX = amt + 1
#     dp =[[0]*(amt + 1) for _ in range(n+1)]
#     for a in range(1,amt + 1):
#         dp[0][a] = MAX
#     for i in range(1,n+1):
#         for a in range(1,amt+1):
#             if coins[i-1] > a:
#                 dp[i][a] = dp[i-1][a]
#             else:
#                 dp[i][a] = min(dp[i-1][a],dp[i][a-coins[i-1]]+1)
#     return dp[n][amt] if dp[n][amt] < MAX else -1

# if __name__ == "__main__":
#     coins = [1, 2, 5]
#     amt = 11
#     res = coin_change_dp(coins, amt)
#     print(res)

#空间优化
# def coin_change_dp_comp(coins: list[int], amt: int) -> int:
#     n = len(coins)
#     MAX = amt + 1
#     dp = [MAX] * (amt + 1)
#     dp[0] = 0
#     for a in range(1, amt + 1):
#         for i in range(1, n + 1):
#             if coins[i - 1] > a:
#                 dp[a] = dp[a]
#             else:
#                 dp[a] = min(dp[a], dp[a - coins[i - 1]] + 1)
#     return dp[amt] if dp[amt] < MAX else -1
#
# if __name__ == "__main__":
#     coins = [1, 2, 5]
#     amt = 11
#     res = coin_change_dp_comp(coins, amt)
#     print(res)

#零钱兑换问题二
# def coin_change_ii_dp(coins: list[int],amt : int)-> int:
#     n = len(coins)
#     dp = [[0] * (amt + 1) for _ in range(n + 1)]
#     for i in range(n + 1):
#         dp[i][0] = 1
#     for i in range(1, n + 1):
#         for a in range(1,amt +1):
#             if coins[i-1] > a:
#                 dp[i][a] = dp[i-1][a]
#             else:
#                 dp[i][a] = dp[i-1][a] + dp[i][a-coins[i-1]]
#     return dp[n][amt]
#
#
# if __name__ == "__main__":
#     coins = [1,2,5]
#     amt = 5
#
#     res = coin_change_ii_dp(coins,amt)
#     print(res)

#编辑距离问题
# def edit_distance_dp(s: str, t: str) -> int:
#     n, m = len(s), len(t)
#     # dp[i][j] 表示 s 前 i 个字符与 t 前 j 个字符的编辑距离
#     dp = [[0] * (m + 1) for _ in range(n + 1)]
#     for i in range(1, n + 1):
#         dp[i][0] = i
#     for j in range(1, m + 1):
#         dp[0][j] = j
#     for i in range(1, n + 1):
#         for j in range(1, m + 1):
#             if s[i - 1] == t[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1]
#             else:
#                 # 插入、删除、替换三种操作取最小
#                 dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
#     return dp[n][m]
#
# if __name__ == "__main__":
#     s = "kitten"
#     t = "sitting"
#     res = edit_distance_dp(s, t)
#     print(res)

#空间优化
def edit_distance_dp_comp(s:str ,t:str)-> int:
    n,m = len(s),len(t)
    dp = [0] * (m + 1)
    for j in range(1,m+1):
        dp[j] = j
    for i in range(1,n+1):
        leftup = dp[0]
        dp[0] +=1
        for j in range(1, m + 1):
            temp = dp[j]
            if s[i - 1] == t[j - 1]:
                dp[j] = leftup
            else:
                dp[j] = min(dp[j - 1], dp[j], leftup) + 1
            leftup = temp
    return dp[m]

if __name__ == "__main__":
    s = "kitten"
    t = "sitting"
    res = edit_distance_dp_comp(s, t)
    print(res)