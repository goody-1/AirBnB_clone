#!/usr/bin/python3
""" console unittests """

import console
import os
import unittest
import sys
from models import storage
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand_prompt(unittest.TestCase):
    """ testing the prompt of the console """

    @classmethod
    def setUpClass(self):
        """ set up class test """
        self.typing = console.HBNBCommand()

    @classmethod
    def tearDownClass(self):
        """ To remove The JSON file """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

class TestHBNBCommand_help(unittest.TestCase):
    """ testing the help methods """

    def test_help_EOF(self):
        txt = "a clean way to quit"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(txt, output.getvalue().strip())

    def test_help_quit(self):
        txt = "a clean way to quit"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(txt, output.getvalue().strip())

    def test_help_create(self):
        txt = "Creates a new instance"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(txt, output.getvalue().strip())
