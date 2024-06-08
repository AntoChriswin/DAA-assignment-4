def average_value_of_even_numbers_divisible_by_three(nums):
    filtered_nums = [num for num in nums if num % 6 == 0]
    if not filtered_nums:
        return 0
    return sum(filtered_nums) // len(filtered_nums)

# Example usage
print(average_value_of_even_numbers_divisible_by_three([1, 3, 6, 10, 12, 15]))  # Output: 9
print(average_value_of_even_numbers_divisible_by_three([1, 2, 4, 7, 10]))  # Output: 0
