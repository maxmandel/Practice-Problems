def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    og_len = len(nums)
    extra_val = max(nums) + 1
    seen = []
    i = 0
    while i < og_len:
        if nums[i] == extra_val:
            return i
        elif nums[i] not in seen:
            seen.append(nums[i])
            i += 1
        elif nums[i] in seen:
            nums.pop(i)
            nums.append(extra_val)

    return og_len

### TEST
k = removeDuplicates([0,0,1,1,1,2,2,3,3,4])
