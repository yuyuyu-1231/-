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