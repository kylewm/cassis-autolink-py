# -*- coding: utf-8 -*-

'''unit tests for cassis.py '''

from __future__ import unicode_literals, print_function
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


class CheckShortURL(unittest.TestCase):
    def test_checkname(self):
        self.assertEqual(cassis.auto_link('kevinmarks.com',max_url_length=10), '<a class="auto-link" href="http://kevinmarks.com">kevinmarks…</a>')
        self.assertEqual(cassis.auto_link('kevinmarks.com',max_url_length=20), '<a class="auto-link" href="http://kevinmarks.com">kevinmarks.com</a>')
        self.assertEqual(cassis.auto_link('kevinmarks.com',max_url_length=14), '<a class="auto-link" href="http://kevinmarks.com">kevinmarks.com</a>')
        self.assertEqual(cassis.auto_link('http://kevinmarks.com',max_url_length=10), '<a class="auto-link" href="http://kevinmarks.com">kevinmarks…</a>')
        self.assertEqual(cassis.auto_link('https://kevinmarks.com',max_url_length=20), '<a class="auto-link" href="https://kevinmarks.com">kevinmarks.com</a>')
        self.assertEqual(cassis.auto_link('http://kevinmarks.com',max_url_length=14), '<a class="auto-link" href="http://kevinmarks.com">kevinmarks.com</a>')


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


class CheckFragmentions(unittest.TestCase):
    def test_checkspacestyle(self):
        self.assertEqual(cassis.auto_link('“In the case of digital content, the artifact, once created and published, is not static.” https://kartikprabhu.com/article/marginalia#In%20the%20case%20of%20digital%20content,%20the%20artifact,%20once%20created%20and%20published,%20is%20not%20static.',do_embed=True),'“In the case of digital content, the artifact, once created and published, is not static.” <blockquote class="auto-mention"><a class="auto-link" href="https://kartikprabhu.com/article/marginalia#In%20the%20case%20of%20digital%20content,%20the%20artifact,%20once%20created%20and%20published,%20is%20not%20static"><cite>kartikprabhu.com</cite><p>In the case of digital content, the artifact, once created and published, is not static</p></a></blockquote>.')
    def test_checkplustyle(self):
        self.assertEqual(cassis.auto_link('http://www.kevinmarks.com/mentionquote.html##we+potentially+have+a+quote+from+the+source+in+the+link+itself',do_embed=True),'<blockquote class="auto-mention"><a class="auto-link" href="http://www.kevinmarks.com/mentionquote.html##we+potentially+have+a+quote+from+the+source+in+the+link+itself"><cite>www.kevinmarks.com</cite><p>we potentially have a quote from the source in the link itself</p></a></blockquote>')

if __name__ == '__main__':
    unittest.main()
