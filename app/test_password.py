"""Tests for password.py"""

import os
from subprocess import getstatusoutput, getoutput
import main
prg = './main.py'

# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)

# --------------------------------------------------
def test_min_password_length():
    """default password min is 7"""

    assert main.password_min_length > 7

# --------------------------------------------------
def test_max_password_length():
    """default password max is 16"""

    assert main.password_min_length > 17