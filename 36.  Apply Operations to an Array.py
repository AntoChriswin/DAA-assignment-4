def apply_operations(nums):
    n = len(nums)

    # Step 1: Apply the operations
    for i in range(n - 1):
        if nums[i] == nums[i + 1]:
            nums[i] *= 2
            nums[i + 1] = 0

    # Step 2: Shift zeros to the end
    result = []
    zero_count = 0

    for num in nums:
        if num != 0:
            result.append(num)
        else:
            zero_count += 1

    result.extend([0] * zero_count)

    return result


# Example usage
print(apply_operations([1, 2, 2, 1, 1, 0]))  # Output: [1, 4, 2, 0, 0, 0]
print(apply_operations([0, 1]))  # Output: [1, 0]
