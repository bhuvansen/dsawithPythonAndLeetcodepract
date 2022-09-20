'''
744. Find Smallest Letter Greater Than Target
Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.
Note that the letters wrap around.
For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
'''
class Solution:
    def nextGreatestLetter(self, letters, target):
        left = 0
        right = len(letters) - 1
        while left <= right:
            mid = (left + right) // 2
            if target < letters[mid]:
                right = mid - 1
            else:
                left = mid + 1
        if left==len(letters):
            return letters[0]
        else:
            return letters[left]