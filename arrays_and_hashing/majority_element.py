class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num,0)+1
        majority_element = None
        frequency = 0
        for key in hashmap:
            if hashmap[key]>frequency:
                frequency = hashmap[key]
                majority_element = key
        return majority_element
sol = Solution()
print(sol.majorityElement([5,5,1,1,1,5,5]))