from pylorem.utils.helper import get_data_json

import unittest

class TestGetDataJson(unittest.TestCase):

    # Returns the data from the json file for the given selection.
    def test_returns_data_for_given_selection_with_additional_element(self):
        # Arrange
        expected_data = ["adipiscing", "elit.", "Sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore", "magna", "aliqua.", "Ut", "enim", "ad", "minim", "veniam,", "quis", "nostrud", "exercitation", "ullamco", "laboris", "nisi", "ut", "aliquip", "ex", "ea", "commodo", "consequat.", "Duis", "aute", "irure", "dolor", "in", "reprehenderit", "in", "voluptate", "velit", "esse", "cillum", "dolore", "eu", "fugiat", "nulla", "pariatur.", "Excepteur", "sint", "occaecat", "cupidatat", "non", "proident,", "sunt", "in", "culpa", "qui", "officia", "deserunt", "mollit", "anim", "id", "est", "laborum."]

        # Act
        actual_data = get_data_json("lorem_words")

        # Assert
        self.assertEqual(actual_data, expected_data)

    # Returns the correct data for the default selection 'lorem_words'.
    def test_returns_correct_data_for_default_selection(self):
        # Arrange
        expected_data = ['adipiscing', 'elit.', 'Sed', 'do', 'eiusmod', 'tempor', 'incididunt', 'ut', 'labore', 'et', 'dolore', 'magna', 'aliqua.', 'Ut', 'enim', 'ad', 'minim', 'veniam,', 'quis', 'nostrud', 'exercitation', 'ullamco', 'laboris', 'nisi', 'ut', 'aliquip', 'ex', 'ea', 'commodo', 'consequat.', 'Duis', 'aute', 'irure', 'dolor', 'in', 'reprehenderit', 'in', 'voluptate', 'velit', 'esse', 'cillum', 'dolore', 'eu', 'fugiat', 'nulla', 'pariatur.', 'Excepteur', 'sint', 'occaecat', 'cupidatat', 'non', 'proident,', 'sunt', 'in', 'culpa', 'qui', 'officia', 'deserunt', 'mollit', 'anim', 'id', 'est', 'laborum.']

        # Act
        actual_data = get_data_json()

        # Assert
        self.assertEqual(actual_data, expected_data)
