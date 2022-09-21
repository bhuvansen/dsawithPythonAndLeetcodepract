from re import I


class Solution:
    def cyclicSort(self, nums):
        i=0
        while i<len(nums):
            if nums[nums[i]-1] == nums[i]:
                i+=1
            else:
                correctIndex = nums[i]-1
                temp = nums[i]
                nums[i]=nums[correctIndex]
                nums[correctIndex]=temp
        return nums


sol = Solution()
nums = [5,4,3,2,1]  
print(sol.cyclicSort(nums))
