class Solution:
    def findDuplicate(self, nums) :
        i=0
        while i<len(nums):
            if nums[nums[i]-1] == nums[i]:
                i+=1
            else:
                correctIndex = nums[i]-1
                temp = nums[i]
                nums[i]=nums[correctIndex]
                nums[correctIndex]=temp
        for i in range(len(nums)):
            if nums[i] != i+1:
                return nums[i]
sol = Solution()
nums = [1,3,4,2,2]
print(sol.findDuplicate(nums))
