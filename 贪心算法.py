# def coin_change_greedy(coins: list[int],amt:int):
#     i = len(coins) - 1
#     count = 0
#     while amt > 0:
#         while i > 0 and coins[i] > amt:
#             i -= 1
#         amt -= coins[i]
#         count += 1
#     return count if amt == 0 else -1
#
# if __name__ == '__main__':
#     coins = [1, 2, 5]
#     amt = 11
#     print(coin_change_greedy(coins, amt))

#分数背包问题
# class Item:
#     def __init__(self, w:int,v:int):
#         self.w = w #weight
#         self.v = v #value
#
# def fractional_knapsack(wgt: list[int], val: list[int], cap: int)-> int:
#     items = [Item(w,v) for w,v in zip(wgt,val)]
#     items.sort(key=lambda item: item.v / item.w, reverse=True)
#     res = 0
#     for item in items:
#         if cap >= item.w:
#             cap -= item.w
#             res += item.v
#         else:
#             res += item.v * cap / item.w
#             break
#     return res
#
#
#
# if __name__ == "__main__":
#     wgt = [10,20,30,40,50]
#     val = [50,120,150,210,240]
#     cap = 50
#     n = len(wgt)
#
#     res = fractional_knapsack(wgt,val,cap)
#     print(res)

#最大容量问题
# def max_capacity(ht: list[int])->int:
#     i,j = 0,len(ht)-1
#     res = 0
#     while i < j :
#         cap = min(ht[i],ht[j])*(j-i)
#         res = max(res,cap)
#         if ht[i] < ht[j]:
#             i += 1
#         else:
#             j -= 1
#     return res
# if __name__ == "__main__":
#     ht = [3,8,5,2,7,7,3,4]
#     res = max_capacity(ht)
#     print(res)

#最大切分乘积问题
import math

def max_product_cutting(n: int) -> int :
    if n <= 3:
        return 1*(n-1)
    a,b = n//3, n % 3
    if b == 1:
        return int(math.pow(3,a-1))*2*2
    if b == 2:
        return int(math.pow(3,a))*2
    return int(math.pow(3,a))

if __name__ == "__main__":
    n = 58
    res = max_product_cutting(n)
    print(res)
