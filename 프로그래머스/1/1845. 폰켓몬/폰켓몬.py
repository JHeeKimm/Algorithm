def solution(nums):
    nums_half = len(nums)/2
    arr = []
    for i in nums:
        if i not in arr:
            arr.append(i)
    if len(arr) < nums_half:
        return len(arr)
    return nums_half