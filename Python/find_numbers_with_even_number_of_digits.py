from ast import List


class Solution:
    """
    # Approach 1: Divide by 10 until number becomes 0 and count digits
    # Time Complexity: O(n *log(max num of digits)) where n is array length and d is average digits per number
    # Space Complexity: O(1)
    # Logic: For each number, repeatedly divide by 10 to count digits.
    #        If digit count is even, increment the counter.
    """
    def numberHasEvenDigits(self, num:int)->bool:
        digitcount = 0
        while num!=0:
            num = num//10
            digitcount +=1

        return digitcount%2==0 # True if even, False if odd

    def findNumbers(self, nums: List[int]) -> int:
        even_count = 0
        for num in nums:
            if(self.numberHasEvenDigits(num)):
                even_count+=1

        return even_count
class Solution2:
    """
    # Approach 2: Convert number to string and check length
    # Time Complexity: O(n * d) where n is array length and d is average digits per number
    # Space Complexity: O(1)
    # Logic: Convert each number to string and check if length is even.
    """
    def findNumbers(self, nums: List[int]) -> int:
        even_count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                even_count += 1

        return even_count
if __name__ == "__main__":
    solution = Solution()
    
    # Sample test cases
    test_cases = [
        [12, 345, 2, 6, 7896],
        [555, 901, 482, 1771],
        [1, 22, 333, 4444],
        [1234, 56789, 0, 12]
    ]
    
    for i, nums in enumerate(test_cases, 1):
        result = solution.findNumbers(nums)
        print(f"Test case {i}: {nums}")
        print(f"Output: {result}")
        print()