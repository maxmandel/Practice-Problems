def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    counter = 0
    while counter < k:
        temp_storage = nums[len(nums) - 1]
        for j in range(len(nums)):
            l = len(nums) - 1 - j
            if l != 0:
                nums[l] = nums[l-1]
            else:
                nums[l] = temp_storage
        
        counter += 1

    return None