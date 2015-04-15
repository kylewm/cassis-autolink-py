'''unit tests for cassis.py '''

import cassis
import unittest

class CheckTwitter(unittest.TestCase):
    def test_checkname(self):
        self.assertEqual(cassis.auto_link('@t'), '<a class="auto-link h-x-username" href="https://twitter.com/t">@t</a>')
    def test_checknamewithspace(self):
        self.assertEqual(cassis.auto_link(' @t '), ' <a class="auto-link h-x-username" href="https://twitter.com/t">@t</a> ')
    def test_checknamewithword(self):
        self.assertEqual(cassis.auto_link('hi @t'), 'hi <a class="auto-link h-x-username" href="https://twitter.com/t">@t</a>')
    def test_checknoname(self):
        self.assertEqual(cassis.auto_link('@'), '@')
    def test_checklongname(self):
        self.assertEqual(cassis.auto_link('@kevinmarks'), '<a class="auto-link h-x-username" href="https://twitter.com/kevinmarks">@kevinmarks</a>')
    def test_checklongnamewithspaces(self):
        self.assertEqual(cassis.auto_link(' @kevinmarks '), ' <a class="auto-link h-x-username" href="https://twitter.com/kevinmarks">@kevinmarks</a> ')
    def test_checklongnamewithword(self):
        self.assertEqual(cassis.auto_link('hi @kevinmarks'), 'hi <a class="auto-link h-x-username" href="https://twitter.com/kevinmarks">@kevinmarks</a>')

class CheckURL(unittest.TestCase):
    def test_checkname(self):
        self.assertEqual(cassis.auto_link('kevinmarks.com'), '<a class="auto-link" href="http://kevinmarks.com">kevinmarks.com</a>')
    def test_checknamewithspace(self):
        self.assertEqual(cassis.auto_link(' kevinmarks.com '), ' <a class="auto-link" href="http://kevinmarks.com">kevinmarks.com</a> ')
    def test_checknamewithword(self):
        self.assertEqual(cassis.auto_link('hi kevinmarks.com'), 'hi <a class="auto-link" href="http://kevinmarks.com">kevinmarks.com</a>')
    def test_checknourl(self):
        self.assertEqual(cassis.auto_link('kevinmarks'), 'kevinmarks')
    def test_checknamewithttp(self):
        self.assertEqual(cassis.auto_link('http://kevinmarks.com'), '<a class="auto-link" href="http://kevinmarks.com">http://kevinmarks.com</a>')

class CheckEmail(unittest.TestCase):
    def test_checkemail(self):
        self.assertEqual(cassis.auto_link('kevinmarks@gmail.com'), 'kevinmarks@gmail.com')

class CheckImage(unittest.TestCase):
    def test_checkgif(self):
        self.assertEqual(cassis.auto_link('http://media2.giphy.com/media/it8ZQy0jXZiX6/giphy.gif'), '<a class="auto-link" href="http://media2.giphy.com/media/it8ZQy0jXZiX6/giphy.gif">http://media2.giphy.com/media/it8ZQy0jXZiX6/giphy.gif</a>')
    def test_checksvg(self):
        self.assertEqual(cassis.auto_link('http://svgur.com/i/19.svg'), '<a class="auto-link" href="http://svgur.com/i/19.svg">http://svgur.com/i/19.svg</a>')
    def test_checkgifinline(self):
        self.assertEqual(cassis.auto_link('http://media2.giphy.com/media/it8ZQy0jXZiX6/giphy.gif',True), '<a class="auto-link figure" href="http://media2.giphy.com/media/it8ZQy0jXZiX6/giphy.gif"><img alt="gif" src="http://media2.giphy.com/media/it8ZQy0jXZiX6/giphy.gif"/></a>')
    def test_checksvginline(self):
        self.assertEqual(cassis.auto_link('http://svgur.com/i/19.svg',True), '<a class="auto-link figure" href="http://svgur.com/i/19.svg"><img alt="svg" src="http://svgur.com/i/19.svg"/></a>')

class CheckMixed(unittest.TestCase):
    def test_checkgif(self):
        self.assertEqual(cassis.auto_link('see kevinmarks.com and kevinmarks.com/km.jpg and kevinmarks.com'), 'see <a class="auto-link" href="http://kevinmarks.com">kevinmarks.com</a> and <a class="auto-link" href="http://kevinmarks.com/km.jpg">kevinmarks.com/km.jpg</a> and <a class="auto-link" href="http://kevinmarks.com">kevinmarks.com</a>')

if __name__ == '__main__':
    unittest.main()

