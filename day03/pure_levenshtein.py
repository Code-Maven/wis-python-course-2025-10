"""
Pure Python implementations of Levenshtein distance algorithm.

This module contains two implementations:
1. Space-optimized version (uses O(min(m,n)) space)
2. Classic full-matrix version (uses O(m*n) space, easier to understand)

Both implementations use only Python standard library - no external dependencies.
"""


def levenshtein_optimized(word1, word2):
    """
    Space-optimized pure Python implementation of Levenshtein distance.
    
    Uses only O(min(m,n)) space instead of O(m*n) by keeping only two rows
    of the dynamic programming matrix in memory at once.
    
    Args:
        word1 (str): The first word to compare
        word2 (str): The second word to compare
    
    Returns:
        int: The Levenshtein distance between the two words
    """
    # Convert to lowercase for case-insensitive comparison
    word1 = word1.lower()
    word2 = word2.lower()
    
    # Get the lengths of both words
    len1, len2 = len(word1), len(word2)
    
    # Handle edge cases
    if len1 == 0:
        return len2
    if len2 == 0:
        return len1
    
    # Ensure word1 is the shorter string to minimize space usage
    if len1 > len2:
        word1, word2 = word2, word1
        len1, len2 = len2, len1
    
    # Create two rows for the dynamic programming matrix
    prev_row = list(range(len1 + 1))
    curr_row = [0] * (len1 + 1)
    
    # Fill in the matrix row by row
    for i in range(1, len2 + 1):
        curr_row[0] = i
        
        for j in range(1, len1 + 1):
            # If characters match, no edit needed
            if word2[i-1] == word1[j-1]:
                cost = 0
            else:
                cost = 1
            
            # Calculate minimum cost from three possible operations:
            curr_row[j] = min(
                prev_row[j] + 1,        # deletion
                curr_row[j-1] + 1,      # insertion
                prev_row[j-1] + cost    # substitution
            )
        
        # Swap rows for next iteration
        prev_row, curr_row = curr_row, prev_row
    
    return prev_row[len1]


def levenshtein_classic(word1, word2):
    """
    Classic full-matrix pure Python implementation of Levenshtein distance.
    
    This is the traditional dynamic programming approach that creates
    a full (m+1) x (n+1) matrix. Easier to understand but uses more memory.
    
    Args:
        word1 (str): The first word to compare
        word2 (str): The second word to compare
    
    Returns:
        int: The Levenshtein distance between the two words
    """
    # Convert to lowercase for case-insensitive comparison
    word1 = word1.lower()
    word2 = word2.lower()
    
    # Get the lengths of both words
    len1, len2 = len(word1), len(word2)
    
    # Create a matrix to store the distances
    # matrix[i][j] represents the distance between word1[:i] and word2[:j]
    matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    
    # Initialize the first row and column
    # Distance from empty string to any prefix
    for i in range(len1 + 1):
        matrix[i][0] = i  # Delete all characters from word1
    for j in range(len2 + 1):
        matrix[0][j] = j  # Insert all characters to get word2
    
    # Fill in the rest of the matrix using dynamic programming
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            # Check if characters at current positions match
            if word1[i-1] == word2[j-1]:
                cost = 0  # No operation needed
            else:
                cost = 1  # Substitution needed
            
            # Calculate minimum cost from three possible operations:
            matrix[i][j] = min(
                matrix[i-1][j] + 1,      # deletion from word1
                matrix[i][j-1] + 1,      # insertion into word1
                matrix[i-1][j-1] + cost  # substitution (or match if cost=0)
            )
    
    # Return the distance between the full strings
    return matrix[len1][len2]


def levenshtein_recursive(word1, word2, memo=None):
    """
    Recursive implementation with memoization (for educational purposes).
    
    This shows the recursive nature of the problem but is not efficient
    for large strings without memoization.
    
    Args:
        word1 (str): The first word to compare
        word2 (str): The second word to compare
        memo (dict): Memoization dictionary (used internally)
    
    Returns:
        int: The Levenshtein distance between the two words
    """
    if memo is None:
        memo = {}
    
    # Convert to lowercase for case-insensitive comparison
    word1 = word1.lower()
    word2 = word2.lower()
    
    # Check memoization
    if (word1, word2) in memo:
        return memo[(word1, word2)]
    
    # Base cases
    if len(word1) == 0:
        return len(word2)
    if len(word2) == 0:
        return len(word1)
    
    # If first characters match, solve for the rest
    if word1[0] == word2[0]:
        result = levenshtein_recursive(word1[1:], word2[1:], memo)
    else:
        # Try all three operations and take minimum
        result = 1 + min(
            levenshtein_recursive(word1[1:], word2, memo),      # deletion
            levenshtein_recursive(word1, word2[1:], memo),      # insertion
            levenshtein_recursive(word1[1:], word2[1:], memo)   # substitution
        )
    
    # Memoize the result
    memo[(word1, word2)] = result
    return result


# Demonstration and testing
if __name__ == "__main__":
    import time
    
    # Test cases
    test_cases = [
        ("hello", "hello"),      # Identical
        ("hello", "Hello"),      # Case difference
        ("cat", "bat"),          # One substitution
        ("kitten", "sitting"),   # Classic example
        ("python", "java"),      # Very different
        ("", "abc"),             # Empty string
        ("test", "testing"),     # Insertion
        ("apple", "aple"),       # Deletion
    ]
    
    print("Pure Python Levenshtein Distance Implementations")
    print("=" * 60)
    
    # Test all implementations
    for word1, word2 in test_cases:
        optimized = levenshtein_optimized(word1, word2)
        classic = levenshtein_classic(word1, word2)
        recursive = levenshtein_recursive(word1, word2)
        
        print(f"'{word1}' vs '{word2}':")
        print(f"  Optimized: {optimized}")
        print(f"  Classic:   {classic}")
        print(f"  Recursive: {recursive}")
        
        # Verify all implementations give same result
        assert optimized == classic == recursive, "Implementations don't match!"
        print()
    
    # Performance comparison
    print("Performance Comparison (for 'kitten' vs 'sitting'):")
    print("-" * 50)
    
    test_word1, test_word2 = "kitten", "sitting"
    
    # Time optimized version
    start = time.time()
    for _ in range(10000):
        levenshtein_optimized(test_word1, test_word2)
    optimized_time = time.time() - start
    
    # Time classic version
    start = time.time()
    for _ in range(10000):
        levenshtein_classic(test_word1, test_word2)
    classic_time = time.time() - start
    
    # Time recursive version (fewer iterations due to slower performance)
    start = time.time()
    for _ in range(100):
        levenshtein_recursive(test_word1, test_word2)
    recursive_time = (time.time() - start) * 100  # Scale to compare
    
    print(f"Optimized:  {optimized_time:.4f} seconds (10,000 iterations)")
    print(f"Classic:    {classic_time:.4f} seconds (10,000 iterations)")
    print(f"Recursive:  {recursive_time:.4f} seconds (100 iterations scaled)")
    print()
    print("The optimized version is usually fastest due to better memory locality.")