class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        frequency_s = {}
        frequency_t = {}
        
        for char in s:
            frequency_s[char] = frequency_s.get(char,0) + 1
        for char in t:
            frequency_t[char] = frequency_t.get(char,0) + 1
            
        return frequency_s == frequency_t
sol = Solution()
print(sol.isAnagram('racecar','carrace'))

#BRUTE FORCE APPROACH O(N^2)
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s)!=len(t):
#             return False
            
#         frequency_s = {}
#         for char in s:
#             char_frequency = 0
#             for i in range(len(s)):
#                 if s[i] == char:
#                     char_frequency += 1
#             if char not in frequency_s:
#                 frequency_s[char] = char_frequency
#         frequency_t = {}
#         for char in t:
#             char_frequency = 0
#             for i in range(len(t)):
#                 if t[i] == char:
#                     char_frequency += 1
#             if char not in frequency_t:
#                 frequency_t[char] = char_frequency
#         return frequency_s == frequency_t