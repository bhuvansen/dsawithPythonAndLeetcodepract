'''
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
'''


class Solution:
    def search(self, nums, target) :
      left = 0
      right = len(nums)
      while left<right:
         mid = left + (right-left)//2
         if nums[mid] == target:
            return mid
         if nums[left]<=nums[mid]:
            if target >=nums[left] and target <nums[mid]:
               right = mid
            else:
               left = mid+1
         else:
            if target<=nums[right-1] and target>nums[mid]:
               left = mid+1
            else:
               right = mid
      return -1