class Solution:
    def insertionSort(self, nums):
        for i in range(0, len(nums)-1):
            j = i+1
            while j>0:
                if nums[j]<nums[j-1]:
                    temp = nums[j]
                    nums[j] = nums[j-1]
                    nums[j-1] = temp
                else:
                    break
                j-=1
        return nums



sol = Solution()
nums = [2,1,3,5,4]   
print(sol.insertionSort(nums))
