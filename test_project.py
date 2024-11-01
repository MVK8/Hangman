from project import menu, game_mode, game_maker, theme_maker, game_exit, word_maker
import unittest
from unittest.mock import patch
import io
import csv
import os
import pytest

name = "test"


class TestMenuFunction(unittest.TestCase):
    @patch("builtins.input", side_effect=["4", "1"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_menu_option_1(self, mock_stdout, mock_input):
        result = menu(name)
        self.assertEqual(result, 1)
        output = mock_stdout.getvalue()
        self.assertIn("\033[1mInvalid option, please choose between 1-4\033[0m", output)


def test_game_mode():
    with patch("builtins.input", side_effect=["1"]):
        result = game_mode(1, name)
        assert result == "1.csv"


class TestGameMode(unittest.TestCase):
    @patch("builtins.input", side_effect=["1"])
    def test_valid_input(self, mock_input):
        result = game_mode(1, name)
        self.assertEqual(result, "1.csv")


def test_word_maker():
    x = [
        "britishempire",
        "napoleon",
        "propaganda",
        "cold war",
        "rome",
        "coldwar",
        "crusade",
        "fascism",
        "aztec",
        "columbus",
        "churchill",
    ]
    assert word_maker("1.csv") in x


class TestGameMaker(unittest.TestCase):
    @patch("builtins.input", side_effect=["a", "b", "c", "d", "e", "f", "g"])
    @patch("builtins.print")
    def test_game_lost(self, mock_print, mock_input):
        result = game_maker("word", name)
        self.assertFalse(result)

    @patch("builtins.input", side_effect=["w", "o", "r", "d"])
    @patch("builtins.print")
    def test_game_won(self, mock_print, mock_input):
        result = game_maker("word", name)
        self.assertTrue(result)



def test_theme_maker():
    with patch("builtins.input", side_effect=["testfile", "word1", "word2", "/exit"]):
        with pytest.raises(SystemExit):
            theme_maker()
        with open("testfile.csv", mode="r") as file:
            reader = csv.reader(file)
            rows = list(reader)
            assert rows == [["word1"], ["word2"]]
        os.remove("testfile.csv")

class TestGameExit(unittest.TestCase):
    @patch("sys.exit")
    def test_game_exit(self, mock_exit):
        game_exit(name)
        mock_exit.assert_called_once()

#AAAAAAHHHHH help

