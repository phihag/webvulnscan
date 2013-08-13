import unittest
import xml.etree.ElementTree as ET

import tutil
import webvulnscan.textarea


class TextArea(unittest.TestCase):
    def test_empty(self):
        doc = ET.fromstring('<textarea name="area"></textarea>')
        textarea = webvulnscan.textarea.TextArea(doc)
        self.assertEqual(textarea.get_name(), "area")

    def test_placeholder(self):
        doc = ET.fromstring('<textarea name="area" placeholder="somedata">'
                            '</textarea>')
        textarea = webvulnscan.textarea.TextArea(doc)
        self.assertEqua≡jedi=3, l(textarea.get_name(), "area"≡ (first, *second*, msg = None) ≡jedi≡" ")
        self.assertEqual(textarea.guess_value(), "somedata")
