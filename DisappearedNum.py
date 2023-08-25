class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        
        # Mark the numbers that are present in the list
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
        
        # Find the indices of numbers that are positive, which correspond to missing numbers
        missing_numbers = [i + 1 for i in range(n) if nums[i] > 0]
        
        return missing_numbers
