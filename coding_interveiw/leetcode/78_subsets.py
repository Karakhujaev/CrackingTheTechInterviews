def generate_subsets(index, current_subset, nums, result):
    # Base case: if we've reached the end of the array
    if index == len(nums):
        result.append(current_subset[:])  # Append a copy of the current subset
        return
    
    # Recursive case: two choices for each element
    
    # 1. Exclude the current element
    generate_subsets(index + 1, current_subset, nums, result)
    
    # 2. Include the current element
    current_subset.append(nums[index])
    generate_subsets(index + 1, current_subset, nums, result)
    current_subset.pop()  # Backtrack
    
class Solution:
    def subsets(self, nums):
        result = []
        generate_subsets(0, [], nums, result)
        return result
