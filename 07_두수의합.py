
def twoSum (nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]

def twoSum2 (nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [i, nums_map[target - num]]
        nums_map[num] = i