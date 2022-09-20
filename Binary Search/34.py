'''
34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
'''

class Solution:
    def searchRange(self, nums, target):
        left = 0
        right = len(nums) - 1
        inArray=[-1,-1]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid - 1
                inArray[0] =mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        print(inArray)
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid + 1
                inArray[1] = mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return inArray