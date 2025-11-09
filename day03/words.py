"""
Words module for calculating Levenshtein distance between words using the Levenshtein library.

Required dependency: python-Levenshtein
Install with: pip install python-Levenshtein
"""

try:
    import Levenshtein
except ImportError:
    print("Error: python-Levenshtein library not found.")
    print("Please install it with: pip install python-Levenshtein")
    raise


def compare(word1, word2):
    """
    Calculate the Levenshtein distance between two words using the Levenshtein library.
    
    The Levenshtein distance is the minimum number of single-character edits
    (insertions, deletions, or substitutions) required to change one word into another.
    
    This implementation uses the fast C-based python-Levenshtein library.
    
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
    
    # Use the Levenshtein library to compute distance
    return Levenshtein.distance(word1, word2)


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