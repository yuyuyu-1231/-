import heapq

def top_k_heap(nums:list[int],k:int)->list[int]:
    #基于堆查找数组中元素
    #初始化小顶堆
    heap = []
    #数组k个元素入堆
    for i in range(k):
        heapq.heappush(heap,nums[i])
    #从k+1开始保持堆的的长度
    for i in range(k,len(nums)):
        if nums[i] > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap,nums[i])
    return heap

if __name__ == '__main__':
    nums = [1,3,5,7,2,4,6,8]
    k = 3
    print(top_k_heap(nums,k))