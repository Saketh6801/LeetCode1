# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Assume each solution has exact one solution
#
# Example
# 1:
#
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: Because
# nums[0] + nums[1] == 9, we
# return [0, 1].
# Example
# 2:
#
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]
# Example
# 3:
#
# Input: nums = [3, 3], target = 6
# Output: [0, 1]
#
# Constraints:
#
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only
# one
# valid
# answer
# exists.
#
# Follow - up: Can
# you
# come
# up
# with an algorithm that is less than O(n2) time complexity?

#
# Solution Approch: as we use the teo itreations and we can get ans.but as the problem says that less o(n2)
# we can use dict in python or hashmaps



def twosum(arr,target):
    dict={}
    for i,n in enumerate(nums):
        diff=target-n
        if diff in dict:
            print(dict[diff],i)
        dict[n]=i
nums=[2, 7, 11, 15]
target=9
twosum(nums,target)
print('Hello world')

