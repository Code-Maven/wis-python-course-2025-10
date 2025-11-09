"""
Test program for the compare function in the words module.
This program tests the Levenshtein distance calculation with 15 comprehensive test cases.
"""

from words import compare


def run_test(test_num, word1, word2, expected_distance, description):
    """
    Run a single test case and report the result.
    
    Args:
        test_num (int): Test case number
        word1 (str): First word to compare
        word2 (str): Second word to compare
        expected_distance (int): Expected Levenshtein distance
        description (str): Description of what this test case verifies
    
    Returns:
        bool: True if test passed, False if failed
    """
    actual_distance = compare(word1, word2)
    passed = actual_distance == expected_distance
    
    status = "PASS" if passed else "FAIL"
    print(f"Test {test_num:2d}: [{status}] {description}")
    print(f"         Words: '{word1}' vs '{word2}'")
    print(f"         Expected: {expected_distance}, Got: {actual_distance}")
    
    if not passed:
        print(f"         *** TEST FAILED ***")
    
    print()
    return passed


def main():
    """Run all test cases for the compare function."""
    print("=" * 70)
    print("COMPREHENSIVE TEST SUITE FOR WORDS.COMPARE() FUNCTION")
    print("=" * 70)
    print()
    
    test_cases = [
        # Test 1: Identical words
        (1, "hello", "hello", 0, "Identical words (same case)"),
        
        # Test 2: Case differences
        (2, "Hello", "HELLO", 0, "Identical words (different cases)"),
        
        # Test 3: Single character substitution
        (3, "cat", "bat", 1, "Single character substitution"),
        
        # Test 4: Single character insertion
        (4, "test", "tests", 1, "Single character insertion at end"),
        
        # Test 5: Single character deletion
        (5, "apple", "aple", 1, "Single character deletion (double letter)"),
        
        # Test 6: Empty string vs non-empty
        (6, "", "abc", 3, "Empty string vs 3-character word"),
        
        # Test 7: Non-empty vs empty string
        (7, "xyz", "", 3, "3-character word vs empty string"),
        
        # Test 8: Both empty strings
        (8, "", "", 0, "Both empty strings"),
        
        # Test 9: Multiple edits needed
        (9, "kitten", "sitting", 3, "Multiple edits (classic example)"),
        
        # Test 10: Completely different words
        (10, "python", "java", 6, "Completely different programming languages"),
        
        # Test 11: One word is substring of another
        (11, "run", "running", 4, "One word is substring of another"),
        
        # Test 12: Transposition (swap adjacent characters)
        (12, "form", "from", 2, "Adjacent character transposition"),
        
        # Test 13: Single character words
        (13, "a", "b", 1, "Single character substitution"),
        
        # Test 14: Same length, multiple substitutions
        (14, "house", "mouse", 1, "Same length, single substitution"),
        
        # Test 15: Mixed case with edits needed
        (15, "GitHub", "gitlab", 2, "Mixed case with multiple edits needed")
    ]
    
    passed_tests = 0
    total_tests = len(test_cases)
    
    # Run all test cases
    for test_data in test_cases:
        if run_test(*test_data):
            passed_tests += 1
    
    # Print summary
    print("=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    print(f"Total tests run: {total_tests}")
    print(f"Tests passed: {passed_tests}")
    print(f"Tests failed: {total_tests - passed_tests}")
    print(f"Success rate: {(passed_tests / total_tests) * 100:.1f}%")
    
    if passed_tests == total_tests:
        print("\n🎉 ALL TESTS PASSED! The compare function is working correctly.")
    else:
        print(f"\n❌ {total_tests - passed_tests} test(s) failed. Please check the implementation.")
    
    print("=" * 70)


if __name__ == "__main__":
    main()