
# Make sure the test finds the application code
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

import unittest
from app import string_utils

class TestSubstring(unittest.TestCase):

    def test_equal_substrings(self):
        score:float = string_utils.calculate_match_degree("software engineering","software engineering")
        self.assertEqual(score, 1)    
        
    def test_partial_substrings(self):
        score:float = string_utils.calculate_match_degree("software engineering","building engineering")
        self.assertEqual(score, 0.6)

    def test_no_common_substrings(self):
        """No Common Substring and the degree should be Zero"""
        score:float = string_utils.calculate_match_degree("abcdef","uvwxyz")
        self.assertEqual(score, 0.0)

    # def test_partial_overlap_substrings(self):
    #     """Tests for partial overlap of substrings"""
    #     score:float = string_utils.calculate_match_degree("saikrishna","saithokalakrishna")
    #     expected_score = len("sai")/len("saithokalakrishna")
    #     self.assertEqual(score, expected_score)

    def test_empty_input_string(self):
        """Test for empty input string"""
        score:float = string_utils.calculate_match_degree("","testinput")
        self.assertEqual(score, 0.0)

if __name__ == "__main__":
    unittest.main()
