class Solution:
    def missingNumber(self, nums) :
        i=0
        while i<len(nums):
            if nums[i] ==len(nums):
                i+=1
            elif nums[nums[i]] == nums[i]:
                i+=1
            else:
                correctIndex = nums[i]
                temp = nums[i]
                nums[i]=nums[correctIndex]
                nums[correctIndex]=temp
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
        return len(nums)
sol = Solution()
nums = [3,0,1]
print(sol.missingNumber(nums))
