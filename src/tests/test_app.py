import sys
import os 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..')))

from app import index

def test_index():
    assert index()=="Hello world!"
