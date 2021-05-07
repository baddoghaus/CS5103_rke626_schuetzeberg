import unittest
from unittest import mock, TestCase
import word_stats

class TestWordStats(unittest.TestCase):

# test word_stats.py line_counter()
########################################################    
    # test file with lines >= 0
    def test_lines(self):
        self.assertEqual(word_stats.line_counter("zeroLine.txt"), 0)
        self.assertEqual(word_stats.line_counter("oneLine.txt"), 1)
        self.assertEqual(word_stats.line_counter("twoLine.txt"), 2)

    # test FileNotFoundError for cases when input file does not exist
    def test_file_not_found_error_line_counter(self):
        self.assertRaises(FileNotFoundError, word_stats.line_counter, "notAFile.txt")

    # test TypeError for cases when type passed to line_counter() is not of type str
    def test_type_error_line_counter(self):
        self.assertRaises(TypeError, word_stats.line_counter, 1)
        self.assertRaises(TypeError, word_stats.line_counter, 2.5)
        self.assertRaises(TypeError, word_stats.line_counter, 3.5j)
        self.assertRaises(TypeError, word_stats.line_counter, True)
########################################################    

# test word_stats.py character_counter()
########################################################    
    # test files with characters >= 0
    def test_characters(self):
        self.assertEqual(word_stats.character_counter("zeroCharacter.txt"), 0)
        self.assertEqual(word_stats.character_counter("twoCharacter.txt"), 2)
        self.assertEqual(word_stats.character_counter("threeCharacter.txt"), 3)

    # test FileNotFoundError for cases when input file does not exist
    def test_file_not_found_error_character_counter(self):
        self.assertRaises(FileNotFoundError, word_stats.character_counter, "notAFile.txt")
    
    # test TypeError for cases when type passed to character_counter() is not of type str
    def test_type_error_character_counter(self):
        self.assertRaises(TypeError, word_stats.character_counter, 1)
        self.assertRaises(TypeError, word_stats.character_counter, 2.5)
        self.assertRaises(TypeError, word_stats.character_counter, 3.5j)
        self.assertRaises(TypeError, word_stats.character_counter, True)
########################################################    

# test word_stats.py word_counter()
########################################################
    # test files with words >= 0
    def test_word_counter(self):
        self.assertDictEqual(word_stats.word_counter("zeroWord.txt"), {})
        self.assertDictEqual(word_stats.word_counter("oneWord.txt"), {'one': 1})
        self.assertDictEqual(word_stats.word_counter("twoWord.txt"), {'one': 1, 'two': 1})
  
    # test FileNotFoundError for cases when input file does not exist
    def test_file_not_found_error_word_counter(self):
        self.assertRaises(FileNotFoundError, word_stats.word_counter, "notAFile.txt")

    # test TypeError for cases when type pased to word_counter() is not of type str
    def test_type_error_word_counter(self):
        self.assertRaises(TypeError, word_stats.word_counter, 1)
        self.assertRaises(TypeError, word_stats.word_counter, 2.5)
        self.assertRaises(TypeError, word_stats.word_counter, 3.5j)
        self.assertRaises(TypeError, word_stats.word_counter, True)
########################################################

# test word_stats.py word_replacer()
########################################################
    # test the replacement of a word
    @mock.patch('word_stats.check_output', return_value='dog')
    def test_word_replacer(self, mock_check_output):
        actual_result = word_stats.word_replacer("cow.txt")
        expected_result = 'dog'
        self.assertEqual(expected_result, actual_result)
        with open("cow.txt", "w") as in_file:
            in_file.write("cow")
          
    # test FileNotFoundError for cases when input file does not exist
    def test_file_not_found_error_word_replacer(self):
        self.assertRaises(FileNotFoundError, word_stats.word_replacer, "notAFile.txt")

    # test TypeError for cases when type pased to word_replacer() is not of type str
    def test_type_error_word_replacer(self):
        self.assertRaises(TypeError, word_stats.word_replacer, 1)
        self.assertRaises(TypeError, word_stats.word_replacer, 2.5)
        self.assertRaises(TypeError, word_stats.word_replacer, 3.5j)
        self.assertRaises(TypeError, word_stats.word_replacer, True)
########################################################
