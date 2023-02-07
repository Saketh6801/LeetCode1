# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -231 <= x <= 231 - 1

def reverse(nums):
    nums=str(nums)
    if nums[0]=="-":
        reversed_number= (int("-"+''.join(nums[1:][::-1])))
    else:
        reversed_number=(int(nums[::-1]))
    if reversed_number >= -2**31 and reversed_number <= 2**31 - 1:
        return reversed_number
    else:
         return 0
nums=8079
reverse(nums)
# Time complexity:O(logn)
#Space complexity: O(1)
