def min_operations_to_sort(nums):
    n = len(nums)
    target = list(range(1, n)) + [0] if nums.index(0) != 0 else [0] + list(range(1, n))

    pos = {num: i for i, num in enumerate(nums)}
    visited = [False] * n
    operations = 0

    for i in range(n):
        if visited[i] or nums[i] == target[i]:
            continue

        cycle_length = 0
        x = i

        while not visited[x]:
            visited[x] = True
            x = pos[target[x]]
            cycle_length += 1

        if cycle_length > 0:
            operations += (cycle_length - 1)

    return operations

# Example usage
print(min_operations_to_sort([4, 2, 0, 3, 1]))  # Output: 3
print(min_operations_to_sort([1, 2, 3, 4, 0]))  # Output: 0
print(min_operations_to_sort([1, 0, 2, 4, 3]))  # Output: 2
