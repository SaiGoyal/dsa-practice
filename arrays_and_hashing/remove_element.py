class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = len(nums)
        i=0
        while i < k:
            if nums[i]==val:
                nums[i] = nums[k-1]
                k-=1
            else:
                i+=1
        return k
sol = Solution()
print(sol.removeElement([0,1,2,2,3,0,4,2], 2))

#two pointer approach
# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
#         k = 0
#         for num in nums:
#             if num != val:
#                 nums[k]=num
#                 k+=1
#         return k