class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        k = len(s)
        while i<k:
            s[i],s[k-1] = s[k-1],s[i]
            i+=1
            k-=1
