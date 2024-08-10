import pytest


@pytest.mark.parametrize("module",
    ['aggregation', 'cache', 'datastruct', 'deprecation', 'hash', 'helper', 'io', 'logging', 'math', 'pickle', 'profiling', 'sequences',
     'string', 'time', 'typing', 'version'])
def test_import_module(module):
    """
    Make sure all main modules can be imported without any dependencies
    """
    exec(f"from sensai.util import {module}")
