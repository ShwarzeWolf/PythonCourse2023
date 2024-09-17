nums = [1, 1, 2, 3, 3, 5, 4, 5, 4]
nums_without_pairs = set(nums)
for num in nums_without_pairs:
    n = nums.count(num)
    if n == 1:
        print(num)
