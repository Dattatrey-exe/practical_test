#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.

from typing import List

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        # Return an empty list if no solution is found
        return []

sol = Solution()

nums = [2,7,11,15]
target = 22

result = sol.twoSum(nums, target)
print("Input nums:", nums)
print("Target:",target)
print("Output:", result)

print("Hellow World")

#O/P -
    # Input nums: [2, 7, 11, 15]
    # Target: 22
    # Output: [1, 3]
    # Hellow World