class Solution:
    def sortArray(self, nums):
        for i in range(len(nums)):
            swapHappened = False
            for j in range(1, len(nums)-i):
                if nums[j]<nums[j-1]:
                    temp = nums[j]
                    nums[j]=nums[j-1]
                    nums[j-1]=temp
                    swapHappened = True
            if swapHappened==False:
                break
        return nums

sol = Solution()
nums = [1,2, 5, 4, 3]   
print(sol.sortArray(nums))
