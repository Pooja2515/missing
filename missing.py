from collections import Counter

class Solution:
    def findSmallestInteger(self, nums, value):
        # Count frequency of each number modulo 'value'
        freq = Counter([num % value for num in nums])
        
        mex = 0
        while True:
            r = mex % value
            if freq[r] > 0:
                freq[r] -= 1
                mex += 1
            else:
                break
        return mex

# Example Usage:
sol = Solution()
print(sol.findSmallestInteger([1,-10,7,13,6,8], 5))  # Output: 4
print(sol.findSmallestInteger([1,-10,7,13,6,8], 7))  # Output: 2
