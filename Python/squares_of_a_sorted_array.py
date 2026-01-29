from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i]*nums[i]
        nums.sort()
        return nums      
            
if __name__ == "__main__":
    solution = Solution()
    
    # Sample test cases
    test_cases = [
        [-4, -1, 0, 3, 10],
        [-7, -3, 2, 3, 11],
        [-5, -3, -2, -1],
        [0, 1, 2, 3, 4]
    ]
    
    for i, nums in enumerate(test_cases, 1):
        result = solution.sortedSquares(nums)
        print(f"Test case {i}: {nums}")
        print(f"Output: {result}")
        print()