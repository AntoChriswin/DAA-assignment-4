def next_greater_element_IV(nums):
    n = len(nums)
    answer = [-1] * n
    stack = []

    for i in range(n):
        while stack and nums[stack[-1][0]] <= nums[i]:
            _, first_idx = stack.pop()
            if stack:
                answer[first_idx] = nums[i]
        stack.append((i, i))

    return answer


# Example usage
print(next_greater_element_IV([2, 4, 0, 9, 6]))  # Output: [9, 6, 6, -1, -1]
print(next_greater_element_IV([3, 3]))  # Output: [-1, -1]
