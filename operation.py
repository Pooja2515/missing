class Solution:
    def hasSameDigits(self, s):
        digits = [int(c) for c in s]
        while len(digits) > 2:
            new_digits = []
            for i in range(len(digits) - 1):
                new_digits.append((digits[i] + digits[i+1]) % 10)
            digits = new_digits
        return digits[0] == digits[1]

# Example usage
sol = Solution()
print(sol.hasSameDigits("3902"))  # True
print(sol.hasSameDigits("34789")) # False
