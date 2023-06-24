def arrayPairSum(nums):
    nums.sort()  # Sort the array in ascending order
    max_sum = 0

    # Pair adjacent elements and sum up the smaller elements in each pair
    for i in range(0, len(nums), 2):
        max_sum += nums[i]

    return max_sum

nums = [1, 4, 3, 2]
result = arrayPairSum(nums)

print("Output:", result)
