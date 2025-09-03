"""
Unit and regression test for the mbuild_polybuild package.
"""

# Import package, test suite, and other packages as needed
import mbuild_polybuild
import pytest
import sys
import mbuild as mb

def test_mbuild_polybuild_imported():
    """ Sample test, will always pass so long as import statement worked """
    assert "mbuild_polybuild" in sys.modules
