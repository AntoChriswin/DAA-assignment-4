def words_within_two_edits(queries, dictionary):
    def within_two_edits(word1, word2):
        # Check if two words differ by at most two characters
        if len(word1) != len(word2):
            return False
        count_diffs = sum(1 for a, b in zip(word1, word2) if a != b)
        return count_diffs <= 2

    result = []
    for query in queries:
        for word in dictionary:
            if within_two_edits(query, word):
                result.append(query)
                break
    return result

# Example usage
print(words_within_two_edits(["word","note","ants","wood"], ["wood","joke","moat"]))  # Output: ["word", "note", "wood"]
print(words_within_two_edits(["yes"], ["not"]))  # Output: []
