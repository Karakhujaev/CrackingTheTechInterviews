class Solution:
    def maxArea(self, height):
        # Initialize two pointers, one at the beginning and one at the end of the height array
        left, right = 0, len(height) - 1
        # Initialize maximum area to 0
        max_area = 0
      
        # Use a while loop to iterate until the two pointers meet
        while left < right:
            # Calculate the area formed between the two pointers
            current_area = (right - left) * min(height[left], height[right])
            # Update the maximum area if current_area is larger
            max_area = max(max_area, current_area)
          
            # Move the pointer that points to the shorter line inward,
            # since this might lead to a greater area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
      
        # Return the maximum area found
        return max_area