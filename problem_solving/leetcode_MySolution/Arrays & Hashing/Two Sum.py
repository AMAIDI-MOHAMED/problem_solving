class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Loop through each number in the list
        for i in range(len(nums)):
            # Loop through the numbers after the current number
            for j in range(i + 1, len(nums)):
                # If the sum of two numbers equals the target, return their indices
                if nums[i] + nums[j] == target:
                    return [i, j]
        # Return an empty list if no solution is found
        return []  
# Time and Space Complexity:
# Time Complexity: O(n2)
# Space Complexity:O(1)
# Solution by Mohamed Amaidi: A simple brute force approach to the "Two Sum" problem. 