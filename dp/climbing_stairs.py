'''
Problem Statement: Given a number of stairs. 
Starting from the 0th stair we need to climb to the “Nth” stair. 
At a time we can climb either one or two steps. 
We need to return the total number of distinct ways to reach from 0th to Nth stair.
'''
#Memoization technique
def solve(dp, ind):
     
    if ind == 0 or ind == 1:
        return 1
    
    if dp[ind]!=-1:
        return dp[ind]
     
    dp[ind] = solve(dp, ind-1) +  solve(dp, ind-2)

    return dp[ind]

#Tabulation technique
def solve_tabulation(dp, n):

    dp[0]=1
    dp[1]=1

    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]
     
if __name__ == '__main__':
     n = 4
     dp = [-1] * (n + 1)
     print(solve(dp,n))
     print(solve_tabulation(dp,n))



    