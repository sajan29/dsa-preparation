'''
Maximum sum of non-adjacent elements (DP 5)

Problem Statement: Given an array of N positive integers, 
we need to return the maximum sum of the subsequence 
such that no two elements of the subsequence are adjacent elements in the array.

Note: A subsequence of an array is a list with elements of the array 
where some elements are deleted (or not deleted at all) and the elements 
should be in the same order in the subsequence as in the array.

Input: nums = [1, 2, 4]
Output: 5
Explanation: 
Subsequence {1,4} gives maximum sum.

Input:  [2, 1, 4, 9]
Output: 11
Explanation: 
Subsequence {2,9} gives maximum sum

'''
def max_sum_of_nonadjelements(arr, ind, dp):


    if ind == 0:
        return arr[ind]
    if dp[ind] != -1:
        return dp[ind]
    
    pick = 0
    if ind > 2:
        pick =  max_sum_of_nonadjelements(arr, ind-2, dp) + arr[ind]
    notPick = max_sum_of_nonadjelements(arr, ind-1, dp)
    dp[ind] = max(pick,notPick)
    return dp[ind]

arr = [2, 1, 4, 9]
n = len(arr)-1
dp = [-1]* (n+1)
print(max_sum_of_nonadjelements(arr, n, dp))


