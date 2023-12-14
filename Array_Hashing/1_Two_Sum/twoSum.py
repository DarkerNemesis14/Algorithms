class Solution(object):
    def twoSum(self, nums, target):
        hashTable = dict()

        for i in range(len(nums)):
            if target - nums[i] in hashTable:
                return [hashTable[target - nums[i]], i]
            else:
                hashTable[nums[i]] = i