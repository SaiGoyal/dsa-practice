class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        num_set = set()

        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)
        return False

sol1 = Solution()
print(sol1.hasDuplicate([1,2,3,4]))