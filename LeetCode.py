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