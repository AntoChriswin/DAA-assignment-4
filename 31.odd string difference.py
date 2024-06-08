def odd_string(words):
    # Step 1: Create a list to store the difference arrays and a map for counting occurrences
    diff_arrays = []
    diff_map = {}

    # Step 2: Calculate difference arrays for each word
    for word in words:
        diff = []
        for j in range(len(word) - 1):
            diff.append(ord(word[j + 1]) - ord(word[j]))
        diff_arrays.append(diff)
        diff_tuple = tuple(diff)

        # Step 3: Use a dictionary to count occurrences of each difference array
        if diff_tuple in diff_map:
            diff_map[diff_tuple] += 1
        else:
            diff_map[diff_tuple] = 1

    # Step 4: Identify the unique difference array
    unique_diff = None
    for diff_tuple, count in diff_map.items():
        if count == 1:
            unique_diff = diff_tuple
            break

    # Step 5: Find and return the corresponding word
    for i, diff in enumerate(diff_arrays):
        if tuple(diff) == unique_diff:
            return words[i]


# Example usage
print(odd_string(["adc", "wzy", "abc"]))  # Output: "abc"
print(odd_string(["aaa", "bob", "ccc", "ddd"]))  # Output: "bob"
