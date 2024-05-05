import pytest
from hello import hello

def test_hello():
    result = hello()
    assert result in ['Hello, world!', 'Hello, Python!']