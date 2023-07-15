def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    retlst = []
    for idx1, num in enumerate(nums):
        search = target - num
        new_nums = nums[idx1+1:]
        if search in new_nums:
            retlst.append(idx1)
            for idx2, newnum in enumerate(new_nums):
                if newnum == search:
                    retlst.append(idx2+idx1+1)
                    return retlst