import unittest
import pytest
from github import get_user

def test_richkempinski(capsys):
    get_user('richkempinski')
    captured = capsys.readouterr()
    assert captured.out == 'Repo: csp Number of commits : 2\n\
Repo: hellogitworld Number of commits: 30\n\
Repo: helloworld Number of commits: 6\n\
Repo: Mocks Number of commits: 10\n\
Repo: Project1 Number of commits: 2\n\
Repo: richkempinski.github.io Number of commits: 9\n\
Repo: threads-of-life Number of commits: 1\n\
Repo: try_nbdev Number of commits: 2\n\
Repo: try_nbdev2 Number of commits: 5\n'