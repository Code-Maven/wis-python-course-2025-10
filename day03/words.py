def compare(word1, word2):
    """
    Calculate the Levenshtein distance between two words.
    
    The Levenshtein distance is the minimum number of single-character edits
    (insertions, deletions, or substitutions) required to change one word into another.
    
    Args:
        word1 (str): The first word to compare
        word2 (str): The second word to compare
    
    Returns:
        int: The Levenshtein distance between the two words.
             0 means the words are identical.
             Higher values indicate greater differences.
    """
    # Convert to lowercase for case-insensitive comparison
    word1 = word1.lower()
    word2 = word2.lower()
    
    # Get the lengths of both words
    len1, len2 = len(word1), len(word2)
    # this is almost the same as
    # len1 = len(word1)
    # len2 = len(word2)

    # Create a matrix to store the distances
    # Matrix dimensions: (len1 + 1) x (len2 + 1)
    matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    
    # Initialize the first row and column
    # Distance from empty string to any prefix
    for i in range(len1 + 1):
        matrix[i][0] = i
    for j in range(len2 + 1):
        matrix[0][j] = j
    
    # Fill in the rest of the matrix
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            # If characters match, no edit needed
            if word1[i-1] == word2[j-1]:
                cost = 0
            else:
                cost = 1
            
            # Calculate minimum cost from three possible operations:
            # 1. Deletion: matrix[i-1][j] + 1
            # 2. Insertion: matrix[i][j-1] + 1
            # 3. Substitution: matrix[i-1][j-1] + cost
            matrix[i][j] = min(
                matrix[i-1][j] + 1,      # deletion
                matrix[i][j-1] + 1,      # insertion
                matrix[i-1][j-1] + cost  # substitution
            )
    
    # Return the final distance
    return matrix[len1][len2]


# Example usage and testing
if __name__ == "__main__":
    # Test the compare function with various word pairs
    test_cases = [
        ("hello", "hello"),      # Identical words
        ("hello", "Hello"),      # Case difference
        ("cat", "bat"),          # One character substitution
        ("kitten", "sitting"),   # Multiple edits
        ("apple", "aple"),       # One deletion
        ("test", "tests"),       # One insertion
        ("", "abc"),             # Empty string
        ("abc", ""),             # Empty string
        ("python", "java"),      # Completely different
        ("house", "mouse"),      # One substitution
    ]
    
    print("Testing the compare function (Levenshtein distance):")
    print("=" * 60)
    
    for word1, word2 in test_cases:
        distance = compare(word1, word2)
        print(f"Distance between '{word1}' and '{word2}': {distance}")
    
    print("\n" + "=" * 60)
    print("Distance interpretation:")
    print("0 = Identical words (ignoring case)")
    print("1 = Very similar (one edit needed)")
    print("2+ = Increasingly different")