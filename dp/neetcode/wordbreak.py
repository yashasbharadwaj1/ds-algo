class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*(len(s)+1)
        dp[len(s)]=True
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if (i+len(w)) <=len(s) and s[i:i+len(w)]==w:
                    dp[i] =dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]
"""
  timecomplexity: O(n^3)
 There are two nested loops, and substring computation at each iteration. Overall that results in O(n^3)

Space complexity : O(n). Length of dp array is s+1

"""
