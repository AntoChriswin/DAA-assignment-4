def min_non_negative_integer_to_make_beautiful(n, target):
    def digit_sum(x):
        return sum(int(d) for d in str(x))

    # If the initial digit sum of n is already <= target, return 0
    if digit_sum(n) <= target:
        return 0

    # Otherwise, find the minimum x to make n + x beautiful
    x = 0
    factor = 1

    while digit_sum(n + x) > target:
        # Add to x to make n "round up" to the next power of 10
        x += factor
        factor *= 10

        # Ensure to round n to the nearest higher number like 10, 100, etc.
        while (n + x) % factor != 0:
            x += factor // 10

    return x


# Example usage
print(min_non_negative_integer_to_make_beautiful(16, 6))  # Output: 4
print(min_non_negative_integer_to_make_beautiful(467, 6))  # Output: 33
print(min_non_negative_integer_to_make_beautiful(1, 1))  # Output: 0
