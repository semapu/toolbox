"""
Author: Sergi Mas-Pujol
Last update: 13/11/2022

Test related to functionalities for the Notebooks
"""

import unittest
import sys
sys.path.append('.')
sys.path.append('..')
from remove_clean.notebooks import clean_notebooks


class CleanNotebookTest(unittest.TestCase):
    def test_clean_notebook_invalid_directory(self):
        self.assertRaises(ValueError, clean_notebooks, "hola")


if __name__ == '__main__':
    unittest.main()
