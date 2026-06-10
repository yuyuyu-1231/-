# def selection_sort(nums:list[int]):
#     """选择排序"""
#     n = len(nums)
#     for i in range(n-1):
#         k = i
#         for j in range(i+1,n):
#             if nums[j]<nums[k]:
#                 k=j
#         nums[k],nums[i] = nums[i],nums[k]
#
# if __name__ == "__main__":
#     nums = [4,2,3,1,5,2]
#     selection_sort(nums)
#     print(nums)

"""冒泡排序，和优化"""
# def bubble_sort(nums:list[int]):
#     n = len(nums)
#     for i in range(n-1,0,-1):
#         flag = False
#         for j in range(i):
#             if nums[j] > nums[j+1]:
#                 nums[j],nums[j+1] = nums[j+1],nums[j]
#                 flag = True
#         if not flag:
#             break
#
#
# if __name__ == "__main__":
#     nums = [4,1,3,1,5,2]
#     bubble_sort(nums)
#     print(nums)

# """插入排序"""
# def insertion_sort(nums:list[int]):
#     for i in range(1,len(nums)):
#         base = nums[i]
#         j=i-1
#         while j>=0 and nums[j]>base:
#             nums[j+1] = nums[j]
#             j-=1
#         nums[j+1] = base
#
# if __name__ == "__main__":
#     nums = [4,1,3,1,5,2]
#     insertion_sort(nums)
#     print(nums)

# """快速排序"""
# def partition(nums:list[int],left:int,right:int) -> int:
#     #以left为基准数
#     i,j = left ,  right
#     while i<j:
#         while i<j and nums[j]>=nums[left]:
#             j-=1
#         while i<j and nums[i]<=nums[left]:
#             i+=1
#         nums[i],nums[j] = nums[j],nums[i]
#     nums[i],nums[left] = nums[left],nums[i]
#     return i
# #对子数组在进行哨兵划分
# def quick_sort(nums:list[int],left:int,right:int):
#     if left >= right:
#         return
#     pivot = partition(nums,left,right)
#     #递归左右数组
#     quick_sort(nums,left,pivot-1)
#     quick_sort(nums,pivot+1,right)
#
#
# if __name__ == "__main__":
#     # 测试普通情况
#     nums = [2,4,1,0,3,5]
#     quick_sort(nums,0,len(nums)-1)
#     print("普通情况:", nums)
#
#     # 测试完全倒序情况
#     nums_desc = [5,4,3,2,1]
#     quick_sort(nums_desc,0,len(nums_desc)-1)
#     print("倒序情况:", nums_desc)
#
#     # 测试完全正序情况
#     nums_asc = [1,2,3,4,5]
#     quick_sort(nums_asc,0,len(nums_asc)-1)
#     print("正序情况:", nums_asc)

"""快速排序的基准数优化"""
# def median_three(nums:list[int],left:int,mid:int,right:int) -> int:
#     l,m,r = nums[left] ,nums[mid],nums[right]
#     if (l <= m <= r) or (r <= m <= l):
#         return mid
#     if (m <= l <= r) or (r <= l <= m):
#         return left
#     return right
# def partition(nums: list[int], left: int, right: int):
#     med = median_three(nums, left, (left + right) // 2, right)
#     nums[left],nums[med] = nums[med],nums[left]
#     i,j = left ,  right
#     while i<j:
#         while i<j and nums[j]>=nums[left]:
#             j-=1
#         while i<j and nums[i]<=nums[left]:
#             i+=1
#         nums[i],nums[j] = nums[j],nums[i]
#     nums[i],nums[left] = nums[left],nums[i]
#     return i
#
# #递归优化
# def quick_sort(nums:list[int],left:int,right:int):
#     while left < right:
#         pivot = partition(nums, left, right)
#         if pivot - left < right - pivot:
#             quick_sort(nums, left, pivot - 1)
#             left = pivot + 1
#         else:
#             quick_sort(nums, pivot + 1, right)
#             right = pivot - 1
#
# if __name__ == "__main__":
#     # 中位基准数优化
#     nums = [2, 4, 1, 0, 3, 5]
#     quick_sort(nums, 0, len(nums) - 1)
#     print("快速排序（中位基准数优化）完成后 nums =", nums)

"""归并排序"""
# def merge(nums:list[int],left:int,mid:int,right:int):
#     tmp = [0] * (right - left + 1)
#     i,j,k = left ,mid+1 , 0
#     while i<=mid and j<=right:
#         if nums[i] <= nums[j]:
#             tmp[k] = nums[i]
#             i+=1
#         else:
#             tmp[k] = nums[j]
#             j+=1
#         k+=1
#
#     while i <= mid:
#         tmp[k] = nums[i]
#         i+=1
#         k+=1
#     while j <= right:
#         tmp[k] = nums[j]
#         j+=1
#         k+=1
#     for k in range(0,len(tmp)):
#         nums[left+k] = tmp[k]
#
# def merge_sort(nums:list[int],left:int,right:int):
#     if left >= right:
#         return
#     mid = (left + right) // 2
#     merge_sort(nums,left,mid)
#     merge_sort(nums,mid+1,right)
#     merge(nums,left,mid,right)
#
# if __name__ == "__main__":
#     nums = [2,4,1,0,3,5]
#     merge_sort(nums,0,len(nums)-1)
#     print(nums)
"""堆排序"""
def sift_down(nums:list[int],n:int,i:int):
    while True:
        l = 2*i+1
        r = 2*i+2
        ma = i
        if l<n and nums[l]>nums[ma]:
            ma = l
        if r<n and nums[r]>nums[ma]:
            ma = r
        if ma == i:
            break
        nums[i],nums[ma] = nums[ma],nums[i]
        i = ma

def heap_aort(nums:list[int]):
    for i in range(len(nums)//2-1,-1,-1):
        sift_down(nums,len(nums),i)
    for i in range(len(nums)-1,0,-1):
        nums[i],nums[0] = nums[0],nums[i]
        sift_down(nums,i,0)

if __name__ == "__main__":
    nums = [2,4,1,0,3,5]
    heap_aort(nums)
    print(nums)

