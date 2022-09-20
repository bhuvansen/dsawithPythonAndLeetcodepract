'''
1095. Find in Mountain Array
(This problem is an interactive problem.)

You may recall that an array arr is a mountain array if and only if:
    -arr.length >= 3
    -There exists some i with 0 < i < arr.length - 1 such that:
    -arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    -arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

Example 1:

Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
'''



# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr):
        left = 0
        right = mountain_arr.length() - 1
        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid)>mountain_arr.get(mid+1):
                if mountain_arr.get(mid)>mountain_arr.get(mid-1):
                    left = mid
                    break
                right = mid - 1
            else:
                left = mid + 1
        
        forFuture = left
        right = forFuture
        left = 0
        while left <= right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) == target:
                return mid
            elif target < mountain_arr.get(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        right = mountain_arr.length() - 1
        left = forFuture
        while left <= right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) == target:
                return mid
            elif target < mountain_arr.get(mid):
                left = mid + 1 
            else:
                right = mid - 1

        return -1