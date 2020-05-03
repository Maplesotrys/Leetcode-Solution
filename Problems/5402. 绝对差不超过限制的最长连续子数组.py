def longestSubarray2(nums, limit):
    left = 0
    right = 0
    res = 0
    max_ = 0
    min_ = 0
    while right < len(nums):
        max_ = max(nums[left:right+1])
        min_ = min(nums[left:right+1])
        if max_ - min_ <=limit:
            res = max(res, right - left + 1)
        right += 1
        while max_ - min_ > limit and left < right:
            left += 1
            max_ = max(nums[left:right + 1])
            min_ = min(nums[left:right + 1])    
    return res
