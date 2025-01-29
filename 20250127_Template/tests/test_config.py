#import statements
import os
import sys


# Add the parent directory of Pyro_DataAnalysis to the system path
sys.path.insert(0, os.path.abspath('Example_template'))
# Import the module
from Example_template.config import *


def test_technical_dir_path():
    result = os.path.exists(technical_dir_path)
    assert result == True

