from unittest import TestCase
from . import converter


class TestConverter(TestCase):
    def test_convert_p(self):
        self.assertEqual(converter.convert_p(
            ['a', 'b']), ['<p>a<br/>b</p>'])
        self.assertEqual(converter.convert_p(
            ['   a  ', ' b ']), ['<p>a<br/>b</p>'])
        self.assertEqual(converter.convert_p(
            ['a', '', 'b']), ['<p>a</p>', '<p>b</p>'])
        self.assertEqual(converter.convert_p(
            ['a', '', '', 'b']), ['<p>a</p>', '<p>b</p>'])
        self.assertEqual(converter.convert_p(
            ['a', '', '', '', 'b']), ['<p>a</p>', '<p>b</p>'])
        self.assertEqual(converter.convert_p(
            ['abc', 'def']), ['<p>abc<br/>def</p>'])
        self.assertEqual(converter.convert_p(
            ['a', '', 'b', '']), ['<p>a</p>', '<p>b</p>'])
        self.assertEqual(converter.convert_p(
            ['a', '', 'b', '', '']), ['<p>a</p>', '<p>b</p>'])
        self.assertEqual(converter.convert_p(
            ['a', '', 'b', '', '', '']), ['<p>a</p>', '<p>b</p>'])
