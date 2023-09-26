def twoSum(self, nums: List[int], target: int) -> List[int]:
    numsList = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in numsList:
            return [numsList[diff], i]
        else:
            numsList[n] = i
    return []  # return an empty list if no solution is found

nums = [2, 5, 4, 2, 55]
target = 7
print(twoSum(nums, target))  # Calling the method on the instance`

