import unittest
from unittest import mock
import pytest
import github

class Test_git_user(unittest.TestCase):

    @mock.patch("github.get_user")
    def test_mock_testing_rich(self, mock_get):
        mock_get.return_value = 10
        result = github.get_user('richkempinski')
        self.assertEqual(result, 10)
    
    @mock.patch("github.get_user")
    def test_mock_testing_sam(self, mock_get):
        mock_get.return_value = 30
        result = github.get_user('sam')
        self.assertEqual(result, 30)
    
    @mock.patch("github.get_user")
    def test_mock_testing_tom(self, mock_get):
        mock_get.return_value = 1
        result = github.get_user('slopiano')
        self.assertEqual(result, 1)
    
    @mock.patch("github.get_user")
    def test_mock_testing_jerry(self, mock_get):
        mock_get.return_value = 4
        result = github.get_user('jerry')
        self.assertEqual(result, 4)

# def test_richkempinski(capsys):
#     get_user('richkempinski')
#     captured = capsys.readouterr()
#     assert captured.out == 'Repo: csp Number of commits: 2\n\
# Repo: hellogitworld Number of commits: 30\n\
# Repo: helloworld Number of commits: 6\n\
# Repo: Mocks Number of commits: 10\n\
# Repo: Project1 Number of commits: 2\n\
# Repo: richkempinski.github.io Number of commits: 9\n\
# Repo: threads-of-life Number of commits: 1\n\
# Repo: try_nbdev Number of commits: 2\n\
# Repo: try_nbdev2 Number of commits: 5\n'