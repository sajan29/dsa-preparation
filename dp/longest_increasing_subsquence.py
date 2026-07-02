'''
Find the length of longest increasing subsequence
nums = [10,9,2,5,3,7,101,18]
length = 4
LIS = [2,3,7,101] or [2,5,7,18]
'''
# Recursion Technique
def lis(curr, prev):

    if curr == len(nums):
        return 0
    not_pick = lis(curr+1,prev)
    pick = 0
    if prev == -1 or nums[prev]>nums[curr]:
        pick = 1 + lis(curr+1,curr)
    
    return max(not_pick,pick)

nums = [10,9,2,5,3,7,101,18]
print(lis(0,-1))
#Memoization technique
dp = {}
def lis_memo(curr, prev):

    if curr == len(nums):
        return 0
    if (curr,prev) in dp:
        return dp[(curr,prev)]
    not_pick = lis_memo(curr+1,prev)
    pick = 0
    if prev == -1 or nums[prev]>nums[curr]:
        pick = 1 + lis_memo(curr+1,curr)
    
    dp[(curr,prev)] = max(not_pick,pick)
    return dp[(curr,prev)]
print(lis_memo(0,-1))
# Binary Search Technique
def lis_binsearch():
    def lower_bound(target, temp):
        left = 0
        right = len(temp)
        while left < right:
            mid = (left+right)//2
            if target <= temp[mid]:
                right = mid - 1
            else:
                left = mid
        return left
    temp = [nums[0]]
    for i in range(1,len(nums)):
        if nums[i]>temp[-1]:
            temp.append(nums[i])
        else:
            temp[lower_bound(nums[i],temp)] = nums[i]
    return len(temp)
print(lis_binsearch())
#[10,9,2,5,3,7,101,18]
#[2,5,7,10,25] insert 9