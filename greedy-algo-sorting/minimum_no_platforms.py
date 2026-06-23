'''
Problem 2: Minimum Railway Platforms

Example:
arr = [900,940,950,1100,1500,1800]
dep = [910,1200,1120,1130,1900,2000]

Goal:

Find the maximum number of overlapping trains at any instant.

Because every overlapping train needs a platform.

Train 1: 900 - 910
Train 2: 940 - 1200
Train 3: 950 - 1120
Train 4: 1100 - 1130
'''

def min_number_platforms(arr, dep):

    i = 1 
    j = 0
    no_of_platforms = 1
    min_no_of_platforms = -1
    n = len(arr)
    while i < n and j < n:
        if arr[i] <= dep[j]:
            no_of_platforms+=1
            min_no_of_platforms = max(no_of_platforms, min_no_of_platforms)
            i+=1
        else:
            no_of_platforms-=1
            j+=1

    return min_no_of_platforms

if __name__ == "__main__":
    arr = [900,940,950,1100,1500,1800]
    dep = [910,1200,1120,1130,1900,2000]
    print(min_number_platforms(arr,dep))