class Solution(object):
    def containsDuplicate(self, nums):
        hash = dict()

        for num in nums:
            if num in hash:
                return True
            else:
                hash[num] = 1
        
        return False