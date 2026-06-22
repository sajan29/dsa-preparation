'''
Problem Statement: Given a number of stairs and a frog, 
the frog wants to climb from the 0th stair to the (N-1)th stair. 
At a time the frog can climb either one or two steps. 
A height[N] array is also given. Whenever the frog jumps from a stair i to stair j, the energy consumed in the jump is abs(height[i]- height[j]), where abs() means the absolute difference. 
We need to return the minimum energy that can be used by the frog to jump from stair 0 to stair N-1..
'''
class Solution:
    # Helper to handle edge cases and start recursion

    def solve(self, ind, height, dp):
        if ind == 0 :
            return 0
        if dp[ind]!= -1:
            return dp[ind]
        
        jumpTwo = int(1e9)
        jumpOne = self.solve(ind-1,height,dp) + abs(height[ind]-height[ind-1])

        if ind > 1:
            jumpTwo = self.solve(ind-2,height,dp) + abs(height[ind]-height[ind-2])
        
        dp[ind] = min(jumpOne,jumpTwo)
        return dp[ind]

    def frogJump(self, height):
        # Handle empty input
        if not height:
            return 0

        # Prepare dp with -1 indicating uncomputed states
        n = len(height)
        dp = [-1] * n

        # Start from the last index
        return self.solve(n - 1, height, dp)

if __name__ == "__main__":
    # Define the heights array
    height = [30, 10, 60, 10, 60, 50]

    # Create Solution instance
    sol = Solution()

    # Compute and print the minimum energy
    print(sol.frogJump(height))  # Expected: 40
