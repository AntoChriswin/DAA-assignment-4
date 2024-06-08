def destroy_sequential_targets(nums, space):
    from collections import defaultdict

    count_map = defaultdict(int)
    for num in nums:
        mod_value = num % space
        count_map[mod_value] += 1

    max_targets = 0
    min_seed = float('inf')
    for num in nums:
        mod_value = num % space
        if count_map[mod_value] > max_targets or (count_map[mod_value] == max_targets and num < min_seed):
            max_targets = count_map[mod_value]
            min_seed = num

    return min_seed

# Example usage
print(destroy_sequential_targets([3, 7, 8, 1, 1, 5], 2))  # Output: 1
print(destroy_sequential_targets([1, 3, 5, 2, 4, 6], 2))  # Output: 1
print(destroy_sequential_targets([6, 2, 5], 100))  # Output: 2
