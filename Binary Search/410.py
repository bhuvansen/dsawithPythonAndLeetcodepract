class Solution:
    def splitArray(self, nums, m):
        n = len(nums)
        start = max(nums)
        end = sum(nums)
        while start + 1< end:
            mid = start + (end - start) // 2
            spliPiece = self.split_into_pieces(nums, mid)
            if spliPiece!=None and spliPiece > m:
                start = mid + 1
            else:
                end = mid
        spliPiece = self.split_into_pieces(nums, start)
        if (spliPiece!=None and spliPiece<= m):
            return start
        return end

    def split_into_pieces(self, nums, largest_sum):
        previous_sum = 0
        pieces = 1
        for num in nums:
            if previous_sum + num > largest_sum:
                previous_sum = num
                pieces += 1
            else:
                previous_sum += num
                
ob1 = Solution()
print(ob1.splitArray([7,2,5,10,8], 2))