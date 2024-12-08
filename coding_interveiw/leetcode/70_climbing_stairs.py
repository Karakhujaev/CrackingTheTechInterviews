class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n

        # Initialize the base cases
        one_step_before = 2
        two_steps_before = 1
        
        # Variable to store the current number of ways
        current = 0
        
        # Use the dynamic programming relation
        for i in range(3, n+1):
            current = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = current
        
        return current

