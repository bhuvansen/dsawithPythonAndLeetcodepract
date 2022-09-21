class Solution:
    def findDuplicates(self, nums) :
        i=0
        while i<len(nums):
            if nums[nums[i]-1] == nums[i]:
                i+=1
            else:
                correctIndex = nums[i]-1
                temp = nums[i]
                nums[i]=nums[correctIndex]
                nums[correctIndex]=temp
        reqList=[]
        for i in range(len(nums)):
            if nums[i] != i+1:
                reqList.append(nums[i])
        return reqList
sol = Solution()
nums = [4,3,2,7,8,2,3,1]
print(sol.findDuplicates(nums))
