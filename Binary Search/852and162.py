'''
852. Peak Index in a Mountain Array
An array arr a mountain if the following properties hold:
    -arr.length >= 3
    -There exists some i with 0 < i < arr.length - 1 such that:
    -arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    -arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.

Example 1:

Input: arr = [0,1,0]
Output: 1
'''


class Solution:
    def peakIndexInMountainArray(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid]>nums[mid+1]:
                if nums[mid]>nums[mid-1]:
                    return mid
                right = mid - 1
            else:
                left = mid + 1
        return left

