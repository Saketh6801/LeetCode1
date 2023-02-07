# 796. Rotate String
# Easy
# 2.5K
# 104
# Companies
# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.
 

# Example 1:

# Input: s = "abcde", goal = "cdeab"
# Output: true
# Example 2:

# Input: s = "abcde", goal = "abced"
# Output: false



# solution:there are two approch.
# solution 1:
class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s)== len(goal) and s in goal+goal:
            return 1
        else:
            return 0
          
          
          
# solution 2:faster than 1
class Solution(object):
    def rotateString(self, s, goal):
       
        for i in range(0,len(s)):
            s=s[1:]+s[0]
            if s==goal:
                return True
        return False
         
