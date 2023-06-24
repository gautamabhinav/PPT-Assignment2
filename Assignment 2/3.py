def findLHS(nums):
    num_freq = {}  # Dictionary to store frequency of numbers
    max_length = 0

    # Count the frequency of each number
    for num in nums:
        num_freq[num] = num_freq.get(num, 0) + 1

    # Check for harmonious subsequences
    for num in num_freq:
        if num + 1 in num_freq:
            length = num_freq[num] + num_freq[num + 1]
            max_length = max(max_length, length)

    return max_length

nums = [1, 3, 2, 2, 5, 2, 3, 7]
result = findLHS(nums)

print("Output:", result)
