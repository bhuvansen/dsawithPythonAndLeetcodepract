class Solution:
    def selectionSort(self, nums):
        for i in range(len(nums)):
            last = len(nums)-i-1
            maxIndex = self.getMaxIndex(nums, 0, last)
            temp = nums[maxIndex]
            nums[maxIndex] = nums[last]
            nums[last] = temp
        return nums


    def getMaxIndex(self, nums, start, last):
        max= start
        for i in range(1, last+1):
            if nums[i]>nums[max]:
                max = i
        return max

sol = Solution()
nums = [1,2, 5, 4, 3]   
print(sol.selectionSort(nums))
