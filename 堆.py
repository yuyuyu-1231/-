class MaxHeap:
    """大顶堆"""

    def __init__(self, nums: list[int]):
        """构造方法"""
        # 将列表元素原封不动添加进堆
        self.max_heap = nums

    def left(self, i: int) -> int:
        """获取左子节点的索引"""
        return 2 * i + 1

    def right(self, i: int) -> int:
        """获取右子节点的索引"""
        return 2 * i + 2

    def parent(self, i: int) -> int:
        """获取父节点的索引"""
        return (i - 1) // 2  # 向下整除

    def swap(self, i: int, j: int):
        """交换元素"""
        self.max_heap[i], self.max_heap[j] = self.max_heap[j], self.max_heap[i]

    def size(self) -> int:
        """获取堆大小"""
        return len(self.max_heap)

    def is_empty(self) -> bool:
        """判断堆是否为空"""
        return self.size() == 0

    def push(self, val: int):
        """元素入堆"""
        # 添加节点
        self.max_heap.append(val)
        # 从底至顶堆化
        self.sift_up(self.size() - 1)

    def sift_up(self, i: int):
        """从节点 i 开始，从底至顶堆化"""
        while True:
            # 获取节点 i 的父节点
            p = self.parent(i)
            # 当"越过根节点"或"节点无须修复"时，结束堆化
            if p < 0 or self.max_heap[i] <= self.max_heap[p]:
                break
            # 交换两节点
            self.swap(i, p)
            # 循环向上堆化
            i = p


"""Driver Code"""
if __name__ == "__main__":
    # 初始化大顶堆
    # 请注意，输入数组已经是一个已经是一个合法的堆
    max_heap = MaxHeap([9, 8, 6, 6, 7, 5, 2, 1, 4, 3, 6, 2])

    # 元素入堆
    val = 7
    max_heap.push(val)