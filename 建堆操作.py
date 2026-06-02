class MaxHeap:
    """大顶堆（最大堆）：每个节点的值都大于或等于其子节点的值"""

    def __init__(self, nums: list[int]):
        """构造方法，根据输入列表建堆"""
        # 将列表元素原封不动添加进堆（此时还不是合法的堆结构）
        self.max_heap = nums
        # 从最后一个非叶子节点开始，自底向上对每个节点执行下沉操作
        # self.size() - 1 是最后一个元素的索引
        # self.parent(self.size() - 1) 是最后一个非叶子节点的索引
        # 倒序遍历到根节点（索引0），确保每个子树都满足堆性质
        for i in range(self.parent(self.size() - 1), -1, -1):
            self.sift_down(i)

    def left(self, i: int) -> int:
        """获取左子节点的索引：对于索引i的节点，左子节点索引为 2*i + 1"""
        return 2 * i + 1

    def right(self, i: int) -> int:
        """获取右子节点的索引：对于索引i的节点，右子节点索引为 2*i + 2"""
        return 2 * i + 2

    def parent(self, i: int) -> int:
        """获取父节点的索引：对于索引i的节点，父节点索引为 (i-1) // 2（向下整除）"""
        return (i - 1) // 2  # 向下整除

    def swap(self, i: int, j: int):
        """交换堆中索引i和j位置的元素"""
        self.max_heap[i], self.max_heap[j] = self.max_heap[j], self.max_heap[i]

    def size(self) -> int:
        """获取堆的大小（元素个数）"""
        return len(self.max_heap)

    def sift_down(self, i: int):
        """从节点 i 开始，从顶至底堆化（下沉操作）
        核心思想：将节点i与其子节点比较，如果子节点更大则交换，直到满足堆性质
        """
        while True:
            # 计算左右子节点索引，初始化最大值为当前节点i
            l, r, ma = self.left(i), self.right(i), i
            
            # 如果左子节点存在且值大于当前最大值，更新最大值索引为左子节点
            if l < self.size() and self.max_heap[l] > self.max_heap[ma]:
                ma = l
            
            # 如果右子节点存在且值大于当前最大值，更新最大值索引为右子节点
            if r < self.size() and self.max_heap[r] > self.max_heap[ma]:
                ma = r
            
            # 如果最大值仍然是当前节点i，说明已经满足堆性质，无需继续下沉
            if ma == i:
                break
            
            # 交换当前节点与最大值节点（将较大的值上浮）
            self.swap(i, ma)
            
            # 继续处理被交换后的节点（原来的节点i现在在位置ma）
            i = ma


"""Driver Code"""
if __name__ == "__main__":
    # 初始化大顶堆：传入无序列表 [1, 2, 3, 4, 5]
    # 建堆过程会从最后一个非叶子节点开始，依次执行下沉操作
    # 最终得到合法的大顶堆：[5, 4, 3, 1, 2]
    max_heap = MaxHeap([1, 2, 3, 4, 5])