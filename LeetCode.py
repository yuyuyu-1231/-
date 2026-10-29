#无重复字符串最大长度
#滑动窗口+哈希表
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic,res,i = {} , 0 , -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]],i)
            dic[s[j]] = j
            res = max(res,j - i)
        return res
#动态规划+哈希表
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = tmp = 0
        for j in range(len(s)):
            i = dic.get(s[j],-1)
            dic[s[j]]=j
            tmp = tmp + 1 if tmp < j-i else j-i
            res = max(res,tmp)
        return res

#合并两个有序链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dum = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                cur.next , list1 = list1 , list1.next
            else:
                cur.next ,list2 = list2 , list2.next
            cur = cur.next
        cur.next = list1 if list1 else list2
        return dum.next

#反转列表（迭代）
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur , pre = head , None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur =tmp
        return pre

#反转列表（递归）
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recur(cur,pre):
            if not cur: return pre
            res = recur(cur.next,cur)
            cur.next = pre
            return res

        return recur(head,None)

#分隔链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        sml_dummy,big_dummy = ListNode(0),ListNode(0)
        sml ,big = sml_dummy , big_dummy
        while head:
            if head.val < x:
                sml.next = head
                sml = sml.next
            else:
                big.next = head
                big = big.next
            head = head.next
        sml.next = big_dummy.next
        big.next = None
        return sml_dummy.next

#删除链表中的节点
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

#随机链表的复制

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return
        dic = {}
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        return dic[head]

#有效扩号（hashmap）
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s :
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] !=c:
                return False
        return len(stack) == 1
#最小宅
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.min_stack[-1]

    #用宅实现队列
    class MyQueue:

        def __init__(self):
            self.A, self.B = [], []

        def push(self, x: int) -> None:
            self.A.append(x)

        def pop(self) -> int:
            peek = self.peek()
            self.B.pop()
            return peek

        def peek(self) -> int:
            if self.B: return self.B[-1]
            if not self.A: return -1
            while self.A:
                self.B.append(self.A.pop())
            return self.B[-1]

        def empty(self) -> bool:
            return not self.A and not self.B
#字符串编码 解除 反编码
class Solution:
    def decodeString(self, s: str) -> str:
        stack , res , multi = [] , "" , 0
        for c in s:
            if c == "[":
                stack.append([res,multi])
                res , multi = "" , 0
            elif c == "]":
                last_res, cur_multi = stack.pop()
                res = last_res + cur_multi*res
            elif "0"<=c<="9":
                multi = multi * 10 + int(c)
            else:
                res += c
        return res

#同上 （递归算法）
class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s,i):
            res, multi = "",0
            while i < len(s):
                if '0'<= s[i] <= "9":
                    multi = multi*10 +int(s[i])
                elif s[i] == "[":
                    i,tmp= dfs(s,i+1)
                    res += multi *tmp
                    multi = 0
                elif s[i]=="]":
                    return i,res
                else:
                    res += s[i]
                i += 1
            return res
        return dfs(s,0)

#用堆找中位数
from heapq import *
class MedianFinder:

    def __init__(self):
        self.A =[]
        self.B =[]

    def addNum(self, num: int) -> None:
        if len(self.A) != len(self.B):
            heappush(self.A,num)
            heappush(self.B,-heappop(self.A))
        else:
            heappush(self.B,-num)
            heappush(self.A,-heappop(self.B))
    def findMedian(self) -> float:
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0]-self.B[0])/2.0

#优化上码
from heapq import *

class MedianFinder:
    def __init__(self):
        self.A = [] # 小顶堆，保存较大的一半
        self.B = [] # 大顶堆，保存较小的一半

    def addNum(self, num: int) -> None:
        if len(self.A) != len(self.B):
            heappush(self.B, -heappushpop(self.A, num))
        else:
            heappush(self.A, -heappushpop(self.B, -num))

    def findMedian(self) -> float:
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0

#有效的字母异位字符
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = defaultdict(int)
        for c in s:
            dic[c] += 1
        for c in t:
            dic[c] -= 1
        for val in dic.values():
            if val != 0:
                return False
        return True
#字符串中第一个唯一字符
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for c in s:
            dic[c] = not c in dic
        for i , c in enumerate(s):
            if dic[c] : return i
        return -1
#同构字符串
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t, t2s = {}, {}
        for a,b in zip(s,t):
            if a in s2t and s2t[a] != b or b in t2s and t2s[b] != a:
                return False
            s2t[a] , t2s[b] = b, a
        return True
#判断子序列问题
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        i = 0
        for c in t:
            if s[i] == c:
                i+=1
                if len(s) == i:
                    return True
        return False

#链表中间节点
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

#相交链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A,B = headA,headB
        while  A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A
#两数之和2 -输入有序数组
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i,j = 0,len(numbers) - 1
        while i < j :
            s = numbers[i] +numbers[j]
            if s > target: j -=1
            elif s < target: i += 1
            else: return i+1,j+1
        return []

#环形列表2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast , slow = head ,head
        while True:
            if not (fast and fast.next): return
            fast , slow = fast.next.next,slow.next
            if fast == slow:break
        fast = head
        while fast != slow:
            fast,slow = fast.next ,slow.next
        return fast

    #反转字符串中的单词
    class Solution:
        def reverseWords(self, s: str) -> str:
            s = s.strip()
            i = j = len(s) - 1
            res = []
            while i >= 0:
                while i >= 0 and s[i] != " ": i -= 1
                res.append(s[i + 1:j + 1])
                while i >= 0 and s[i] == " ": i -= 1
                j = i
            return ' '.join(res)
#三数之和（双指针）
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res,k = [],0
        for k in range(len(nums) - 2):
            if nums[k] > 0: break
            if k > 0 and nums[k] == nums[k-1]: continue
            i , j = k + 1,len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i -1]: i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j+1]: j -= 1
                else:
                    res.append([nums[k],nums[j],nums[i]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i -1]: i += 1
                    while i < j and nums[j] == nums[j+1]: j -= 1
        return res

#滑动窗口最大值
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        res , n = [] , len(nums)
        for i ,j in zip(range(1-k,n-k+1),range(n)):
            if i > 0 and deque[0] == nums[i-1]:
                deque.popleft()
            while deque and deque[-1] < nums[j]:
                deque.pop()
            deque.append(nums[j])
            if i >= 0:
                res.append(deque[0])
        return res

#字符串相加
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ''
        i,j,carry = len(num1) - 1 ,len(num2) -1,0
        while i >= 0  or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp//10
            res = str(tmp % 10) + res
            i,j = i -1 , j-1
        return '1'+ res if carry else res
#旋转字符串
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and s in (goal+goal)

#验证栈序列
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack , i = [] , 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack

#z字形变换
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        res = ["" for _ in range(numRows)]
        i , flag = 0 , -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1 :
                flag = -flag
            i += flag
        return "".join(res)

#螺旋矩阵
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix:return []
        l,r,t,b,res = 0 ,len(matrix[0]) - 1 ,0,len(matrix) - 1 ,[]
        while True:
            for i in range(l,r+1): res.append(matrix[t][i])
            t += 1
            if t > b: break
            for i in range(t,b+1): res.append(matrix[i][r])
            r -= 1
            if l > r:break
            for i in range(r, l - 1, -1): res.append(matrix[b][i]) # right to left
            b -= 1
            if t > b: break
            for i in range(b, t - 1, -1): res.append(matrix[i][l]) # bottom to top
            l += 1
            if l > r: break
        return res

#螺旋矩阵2
class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        l, r, t, b = 0, n - 1, 0, n - 1
        mat = [[0 for _ in range(n)] for _ in range(n)]
        num, tar = 1, n * n
        while num <= tar:
            for i in range(l, r + 1): # left to right
                mat[t][i] = num
                num += 1
            t += 1
            for i in range(t, b + 1): # top to bottom
                mat[i][r] = num
                num += 1
            r -= 1
            for i in range(r, l - 1, -1): # right to left
                mat[b][i] = num
                num += 1
            b -= 1
            for i in range(b, t - 1, -1): # bottom to top
                mat[i][l] = num
                num += 1
            l += 1

#旋转图像（拷贝矩阵公式法）
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 深拷贝 matrix -> tmp
        tmp = copy.deepcopy(matrix)
        # 根据元素旋转公式，遍历修改原矩阵 matrix 的各元素
        for i in range(n):
            for j in range(n):
                matrix[j][n - 1 - i] = tmp[i][j]
#同上（原地修改）
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = tmp

#字符串转换整数
class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        if not s: return 0
        res,i,sign = 0,1,1
        int_max , int_min , bndry = 2 ** 31 - 1,-2 ** 31,2 ** 31 // 10
        if s[0] == "-": sign = -1
        elif s[0] != '+': i = 0
        for c in s[i:]:
            if not "0" <= c <= '9':break
            if res > bndry or res == bndry and c > "7":return int_max if sign == 1 else int_min
            res = 10 * res + ord(c) - ord("0")
        return sign * res

#二分查找
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i , j = 0 , len(nums) -1
        while i <= j:
            m = (i+j)//2
            if nums[m] < target: i = m+1
            elif nums[m] > target : j = m -1
            else: return m
        return -1
#第一个错误版本
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i,j = 1,n
        while i <= j:
            m = (i+j)//2
            if isBadVersion(m): j = m - 1
            else: i = m + 1
        return i
#寻找数组的中心下标
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sum_left , sum_right = 0 , sum(nums)
        for i in range(len(nums)):
            sum_right -= nums[i]
            if sum_left == sum_right:
                return i
            sum_left += nums[i]
        return -1
#寻找重复数
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1
#同上
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def next(i):
            return nums[i]
        slow = fast = 0
        while True:
            slow = next(slow)
            fast = next(next(fast))
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = next(slow)
            fast = next(fast)
        return slow
#寻找旋转排序数组中的最小值 II
class Solution:
    def findMin(self, nums: list[int]) -> int:
        i , j = 0 ,len(nums) - 1
        while i < j:
            m = (i+j) // 2
            if nums[m] > nums[j]:i = m + 1
            elif nums[m] < nums[j]:j = m
            else : j-=1
        return nums[i]
#方法2
class Solution:
    def findMin(self, nums: [int]) -> int:
        i, j = 0, len(nums) - 1
        while i < j:
            m = (i + j) // 2
            if nums[m] > nums[j]: i = m + 1
            elif nums[m] < nums[j]: j = m
            else: return min(nums[i:j])
        return nums[i]
#二叉树层序遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root: return []
        res , queue = [] , collections.deque()
        queue.append(root)
        while queue:
            tmp =[]
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp)
        return res
#二叉树的锯齿形层序遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root: return []
        res, deque = [], collections.deque([root])
        while deque:
            tmp = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()
                if len(res) % 2 == 0:
                    tmp.append(node.val)
                else:
                    tmp.appendleft(node.val)
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
            res.append(list(tmp))
        return res
#法二
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res, deque = [], collections.deque()
        deque.append(root)
        while deque:
            tmp = []
            # 打印奇数层
            for _ in range(len(deque)):
                # 从左向右打印
                node = deque.popleft()
                tmp.append(node.val)
                # 先左后右加入下层节点
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
            res.append(tmp)
            if not deque: break # 若为空则提前跳出
            # 打印偶数层
            tmp = []
            for _ in range(len(deque)):
                # 从右向左打印
                node = deque.pop()
                tmp.append(node.val)
                # 先右后左加入下层节点
                if node.right: deque.appendleft(node.right)
                if node.left: deque.appendleft(node.left)
            res.append(tmp)
        return res
#法三
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res , queue = [] , collections.deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp[::-1]if len(res)%2 else tmp)
        return res
#二叉树最近公共祖先
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if not left: return right
        if not right: return left
        return root
#二叉搜索树中第k小的元素
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root):
            if not root: return
            dfs(root.left)
            if self.k == 0: return
            self.k -= 1
            if self.k == 0: self.res = root.val
            dfs(root.right)

        self.k = k
        dfs(root)
        return self.res

#二叉搜索树的最近祖先节点
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if not left: return right
        if not right: return left
        return root
#法二
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root

#数组中的第 K 个最大元素
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[len(nums) - k]


#法二 哨兵划分 + 递归
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums,k):
            pivot =  random.choice(nums)
            big, equal, small = [], [], []
            for num in nums:
                if num > pivot:
                    big.append(num)
                elif num < pivot:
                    small.append(num)
                else:
                    equal.append(num)
            if k <= len(big):
                return quick_select(big,k)
            if k > len(big) + len(equal):
                return quick_select(small,k - len(big) - len(equal))
            else:
                return pivot
        return quick_select(nums,k)

#课程表（广度优先搜索+拓扑排序）
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        edges = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for a, b in prerequisites:
            edges[b].append(a)
            indegree[a] += 1

        queue = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        taken = 0
        while queue:
            b = queue.popleft()
            taken += 1
            for a in edges[b]:
                indegree[a] -= 1
                if indegree[a] == 0:
                    queue.append(a)
        return taken == numCourses
#法二（深度优先搜索）
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        def dfs(i, adjacency, flags):
            if flags[i] == -1: return True
            if flags[i] == 1: return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags): return False
            flags[i] = -1
            return True

        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjacency, flags): return False
        return True

#二叉树的最大深度（dfs）
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1
#法二（bfs）
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root: return 0
        queue, res = [root], 0
        while queue:
            tmp = []
            for node in queue:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue = tmp
            res += 1
        return res
#路径总和2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        res, path = [], []

        def recur(root, tar):
            if not root: return
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                res.append(list(path))
            recur(root.left, tar)
            recur(root.right, tar)
            path.pop()

        recur(root, targetSum)
        return res
#全排列
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def dfs(x):
            if x  == len(nums) -1:
                res.append(list(nums))
                return
            for i in range(x,len(nums)):
                nums[i] , nums[x] = nums[x] , nums[i]
                dfs(x + 1)
                nums[i] , nums[x] = nums[x] , nums[i]
        res = []
        dfs(0)
        return res
#全排列2
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        def dfs(x):
            if x == len(nums) - 1:
                res.append(list(nums))
                return
            reen = set()
            for i in range(x,len(nums)):
                if nums[i] in reen:
                    continue
                reen.add(nums[i])
                nums[i] ,nums[x] = nums[x] , nums[i]
                dfs(x+1)
                nums[i] ,nums[x] = nums[x] , nums[i]
        res = []
        dfs(0)
        return res

#组合总和
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(state: list[int], target: int,choices:list[int],start: int,res:list[list[int]]):
            if target == 0:
                res.append(list(state))
                return
            for i in range(start,len(choices)):
                if target - choices[i] < 0:
                    break
                state.append(choices[i])
                backtrack(state, target - choices[i], choices, i, res)
                state.pop()

        state = []
        candidates.sort()
        start = 0
        res = []
        backtrack(state, target,candidates,start,res)
        return res
#组合总和2
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(state:list[int],target:int,choice:list[int],start:int,res:list[list[int]]):
            if target == 0:
                res.append(list(state))
                return
            for i in range(start,len(choice)):
                if target - choice[i] < 0:
                    break
                if i > start and choice[i] == choice[i - 1]:
                    continue
                state.append(choice[i])
                backtrack(state, target - choice[i], choice, i + 1, res)
                state.pop()

        state = []
        candidates.sort()
        start = 0
        res = []
        backtrack(state,target,candidates,start,res)
        return res

#单词搜索
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False
            if k == len(word) - 1: return True
            board[i][j] = " "
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j - 1, k + 1) or dfs(i, j + 1, k + 1)
            board[i][j] = word[k]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        return False

#翻转二叉树（递归）
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return
        tmp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(tmp)
        return root
#法二（队列+交换）
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
         if not root: return
         stack = [root]
         while stack:
            node = stack.pop()
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
            node.left ,node.right = node.right ,node.left
         return root
#对称二叉树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def muves(L, R):
            if not L and not R: return True
            if not L or not R or L.val != R.val: return False
            return muves(L.left, R.right) and muves(L.right, R.left)

        return not root or muves(root.left, root.right)

#pow（x,n）
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0: return 0.0
        res = 1
        if n < 0: x,n = 1/x , -n
        while n:
            if n & 1: res*=x
            x*=x
            n>>= 1
        return res

#平衡二叉树（后序遍历+剪枝）
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def recur(root):
            if not root: return 0
            left = recur(root.left)
            if left == -1:return -1
            right = recur(root.right)
            if right == -1:return -1
            return max(left,right) + 1 if abs(left - right) <= 1 else -1
        return recur(root) != -1

#法二（先序遍历+深度计算）
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        if not root: return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and self.isBalanced(
            root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root: return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

#从前序与中序遍历序列构造二叉树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        def recur(root, left, right):
            # root: 当前子树根在 preorder 中的下标；[left, right]: 当前子树在 inorder 中的区间
            if left > right: return
            node = TreeNode(preorder[root])
            i = dic[preorder[root]]                    # 根节点在 inorder 中的位置
            node.left = recur(root + 1, left, i - 1)   # 左子树：preorder 根后一位 + inorder 左区间
            # 左子树长度 = i - left（inorder 中 [left, i-1] 的元素个数）
            # preorder 顺序为 根 → 左子树(i-left 个) → 右子树，故右子树根 = root + (i - left) + 1
            node.right = recur(i - left + root + 1, i + 1, right)
            return node

        dic, preorder = {}, preorder
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return recur(0, 0, len(inorder) - 1)

#二叉树的序列和反序列
import collections
class Codec:
    def serialize(self, root):
        if not root: return "[]"
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else: res.append("null")
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        if data == "[]": return
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root
#斐波那契数列
class Solution:
    def fib(self, n: int) -> int:
        a,b = 0 , 1
        for _ in range(n):
            a,b = b,a+b
        return a
#爬楼梯
class Solution:
    def climbStairs(self, n: int) -> int:
        a ,b = 1,1
        for _ in range(n-1):
            a,b = b,a+b
        return b
#一维数组的动态和
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        dp =[0] * len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = dp[i-1] + nums[i]
        return dp
#买卖股票的最佳时机
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        cost , profit = float('+inf') , 0
        for price in prices:
            cost = min(cost,price)
            profit = max(profit,price - cost)
        return profit

#最小路径和
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0: continue
                elif i == 0: grid[i][j] = grid[i][j-1] + grid[i][j]
                elif j == 0: grid[i][j] = grid[i-1][j] + grid[i][j]
                else: grid[i][j] = min(grid[i-1][j],grid[i][j-1]) + grid[i][j]
        return grid[-1][-1]

#最大子数组和
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] += max(nums[i-1],0)
        return max(nums)

#打家劫舍
class Solution:
    def rob(self, nums: List[int]) -> int:
        cur, pre = 0, 0
        for num in nums:
            cur, pre = max(pre + num, cur), cur
        return cur
#打家劫舍2
class Solution:
    def rob(self, nums: [int]) -> int:
        def my_rob(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur
        return max(my_rob(nums[:-1]),my_rob(nums[1:])) if len(nums) != 1 else nums[0]
#最长递增子数列
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]: # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
#上题优化
class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num: i = m + 1 # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                else: j = m
            tails[i] = num
            if j == res: res += 1
        return res
#正则表达式匹配
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s)+1, len(p)+1
        dp = [[False]*n for _ in range(m)]
        dp[0][0] = True
        for j in range(2,n,2):
            dp[0][j] = dp[0][j-2] and p[j-1] == '*'
        for i in range(1,m):
            for j in range(1,n):
                if p[j - 1] == '*':
                    if dp[i][j - 2]: dp[i][j] = True
                    elif dp[i - 1][j] and s[i - 1] == p[j - 2]: dp[i][j] = True
                    elif dp[i - 1][j] and p[j - 2] == '.': dp[i][j] = True        # 3.
                else:
                    if dp[i - 1][j - 1] and s[i - 1] == p[j - 1]: dp[i][j] = True # 1.
                    elif dp[i - 1][j - 1] and p[j - 1] == '.': dp[i][j] = True    # 2.
        return dp[-1][-1]

#丑数2
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res , a, b, c = [1] * n , 0, 0, 0
        for i in range(1,n):
            n1,n2,n3 = res[a]*2 ,res[b]*3 , res[c]*5
            res[i] = min(n1,n2,n3)
            if res[i] == n1: a+=1
            if res[i] == n2: b+=1
            if res[i] == n3: c+=1
        return res[-1]

#买卖股票的最佳时机 II
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        for i in range(1,len(prices)):
            tmp = prices[i] - prices[i-1]
            if tmp>0: profit+=tmp
        return profit