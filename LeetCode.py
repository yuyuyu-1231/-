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