class Solution(object):
    def minWindow(self, s, t):  
         need = {}
         for c in t:
            need[c] = need.get(c, 0) + 1
         left = 0
         have = 0
         ans = ""
         for right in range(len(s)):

            if s[right] in need:
                need[s[right]] -= 1
                if need[s[right]] >= 0:
                    have += 1
            while have == len(t):
                if ans == "" or right - left + 1 < len(ans):
                    ans = s[left:right + 1]

                if s[left] in need:
                    need[s[left]] += 1
                    if need[s[left]] > 0:
                        have -= 1
                left += 1
         return ans