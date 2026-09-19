#hashmap approach O(n) space and TC
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

#boyer moore majority voting algorithm O(1) space, O(N) TC
# class Solution:
#     def majorityElement(self, nums: list[int]) -> int:
#         candidate = 0
#         count = 0
#         for num in nums:
#             if count == 0:
#                 candidate = num
#             count += (1 if num == candidate else -1)
#         return candidate
# sol = Solution()
# print(sol.majorityElement([5,5,1,1,1,5,5]))