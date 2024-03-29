class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = dict()

        for num in nums:
            if num in hash:
                return True
            else:
                hash[num] = 1
        
        return False