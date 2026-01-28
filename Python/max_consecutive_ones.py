from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        count = 0
        for num in nums:
            if num==1:
                count+=1
            else:
                maxi = max(count, maxi)
                count = 0

        return max(count, maxi)

if __name__ == "__main__":
    solution = Solution()
    
    # Sample test cases
    test_cases = [
        [1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1],
        [0, 0, 0],
        [1, 1, 1, 1]
    ]
    
    for i, nums in enumerate(test_cases, 1):
        result = solution.findMaxConsecutiveOnes(nums)
        print(f"Test case {i}: {nums}")
        print(f"Output: {result}")
        print()