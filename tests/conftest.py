"""Test configuration"""
import pytest
from module.shared import config_map


@pytest.fixture(scope="session", autouse=True)
def setup():
    """Called at the beginning of the testing session.
    Overrides the test configuration
    """
    # store a copy of the normal configuration
    old_configuration = {}
    for k, val in config_map.items():
        old_configuration[k] = val

    # override normal configuration with test configuration
    for k, val in config_map.get("test", {}).items():
        config_map[k] = val

    yield  # run the tests

    # restore the normal configuration
    for k, val in old_configuration.items():
        config_map[k] = val
