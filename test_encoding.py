import unittest
from encoding import decode
from encoding import garble


class TestEncode(unittest.TestCase):
    def test_for_word_encoding(self):
        self.assertEqual(garble("ala"), "\n-weird-\nala\n-weird-\n")
    def test_for_sentence_encoding(self):
        self.assertEqual(garble("This is a long test,\n with some big word!"),
                         '\n-weird-\nTihs is a lnog tset,\n wtih smoe big wrod!\n-weird-\nlong some test This with word')
    def test_for_special_signs_encoding(self):
        self.assertEqual(garble("!!!@@@###$$$%%%^^^&&&"), "\n-weird-\n!!!@@@###$$$%%%^^^&&&\n-weird-\n")


class TestDecode(unittest.TestCase):
    def test_for_one_word_decode(self):
        self.assertEqual(decode("\n-weird-\n coiknha \n-weird-\n choinka"), 'choinka')
    def test_for_no_word_decode(self):
        self.assertEqual(decode("\n-weird-\n \n-weird-\n"), '')
    def test_for_short_words_decode(self):
        self.assertEqual(decode("\n-weird-\n ala ma raz dwa lat \n-weird-\n"),
                         'ala ma raz dwa lat')
