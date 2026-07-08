'''
A frog wants to climb a staircase with n steps. 
Given an integer array heights, where heights[i] contains the height of the ith step, 
and an integer k. To jump from the ith step to the jth step, 
the frog requires abs(heights[i] - heights[j]) energy, 
where abs() denotes the absolute difference. 
The frog can jump from the ith step to any step in the range [i + 1, i + k], provided it exists. 
Return the minimum amount of energy required by the frog to go from the 0th step to the 
(n-1)th step.
Example 1:
Input: heights = [10, 5, 20, 0, 15], k = 2
Output: 15
Explanation:
0th step -> 2nd step, cost = abs(10 - 20) = 10
2nd step -> 4th step, cost = abs(20 - 15) = 5
Total cost = 10 + 5 = 15.

Example 2:
Input: heights = [15, 4, 1, 14, 15], k = 3
Output: 2
Explanation:
0th step -> 3rd step, cost = abs(15 - 14) = 1
3rd step -> 4th step, cost = abs(14 - 15) = 1
Total cost = 1 + 1 = 2.
'''

def frog_jump_k_dist(heights, k, ind, dp):

    if ind == 0:
        return 0
    if dp[ind]!=-1:
        return dp[ind]
    min_jump = float('inf')
    for j in range(1, k+1):
        if ind-j>=0:
            jump = frog_jump_k_dist(heights, k, ind-j, dp) + abs(heights[ind]-heights[ind-j])
            min_jump = min(jump, min_jump)
    dp[ind]=min_jump
    return dp[ind]
   
heights = [10, 5, 20, 0, 15]
k = 2
n = len(heights)-1
dp = [-1] * (n+1)
print(frog_jump_k_dist(heights, k, n, dp))



