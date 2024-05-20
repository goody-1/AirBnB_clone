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

    def test_docstrings_console(self):
        """console.py docstrings"""
        self.assertTrue(len(console.__doc__) >= 1)

    def test_docstrings_test_console(self):
        """test_console.py doctstrings"""
        self.assertTrue(len(self.__doc__) >= 1)

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class TestHBNBCommand_exit(unittest.TestCase):
    """exiting Test"""

    def test_quit_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


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


class TestHBNBCommand_create(unittest.TestCase):
    """Unittests for testing create from the HBNB command interpreter."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_create_noclass(self):
        errmsg = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(errmsg, output.getvalue().strip())
