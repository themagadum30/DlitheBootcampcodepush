class Solution(object):
    def minWindow(self, s, t):  
         need = {}
         for c in t:
            need[c]=need.get(c,0) + 1
         st=0
         hve=0
         ans=""
         for end in range(len(s)):
            if s[end] in need:
                need[s[end]] -= 1
                if need[s[end]] >= 0:
                 hve+=1
            while hve == len(t):
                if ans=="" or end-st+1<len(ans):
                    ans=s[st:end+1]
                if s[st] in need:
                    need[s[st]] += 1
                    if need[s[st]] > 0:
                     hve -= 1
                st += 1
         return ans