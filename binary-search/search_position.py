'''
1. Search Insert Position

Problem

Given a sorted array of distinct integers nums and a target value target, return:

* The index if the target is found.
* Otherwise, the index where it would be inserted to maintain sorted order.
nums = [1, 3, 5, 6]
target = 5
Answer = 2
'''
def search_insert_position(nums, target):
    left = 0
    right = len(nums)-1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left

'''
2. Find First and Last Position of Element in Sorted Array

Problem

Given a sorted array nums and a target target, return:
[first_occurrence, last_occurrence]
If the target is not present:
[-1, -1]
nums = [5, 7, 7, 8, 8, 10]
target = 8
'''
'''
Similar problems:
Find occurence of the target element within an array
Find occurence of the target element within a range (L,R)
'''
def find_first_and_last_pos(nums, target):
    left = 0
    right = len(nums)
    result = []
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    result.append(left)

    left = 0
    right = len(nums)

    while left < right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
    if result[0] > left - 1:
        result[0]=-1
        result.append(-1)
    else:
        result.append(left-1)
    return result


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 10
    print(find_first_and_last_pos(nums,target))