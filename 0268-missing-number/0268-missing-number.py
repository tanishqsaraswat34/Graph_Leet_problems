class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        if n not in nums:
            return n
        i=0
        while i<=n:
            if i not in nums:
                return i
            i+=1
    
        