def minimumScore(nums, k):
    min_val = min(nums)
    max_val = max(nums)

    scenario1_score = max_val - min_val

    for i in range(len(nums)):
        for x in range(-k, k+1):
            nums[i] += x
            min_val = min(min_val, nums[i])
            max_val = max(max_val, nums[i])
            nums[i] -= x

    scenario2_score = max_val - min_val

    return min(scenario1_score, scenario2_score)

nums = [1]
k = 0
result = minimumScore(nums, k)

print("Output:", result)
