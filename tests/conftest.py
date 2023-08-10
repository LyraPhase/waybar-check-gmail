import os
import sys

import pytest

from waybar_check_gmail.util import XDGBaseDirs

# from pytest_mock import mocker


@pytest.fixture
def input_value():
    input = 234
    print(sys.path)
    return input


@pytest.fixture(scope="module")
def xdg_config_home_env_var() -> pytest.fixture():
    os.environ["XDG_CONFIG_HOME"] = "/home/brubble/.config"
    return os.environ["XDG_CONFIG_HOME"]


@pytest.fixture(scope="module")
def xdg_data_home_env_var() -> pytest.fixture():
    os.environ["XDG_DATA_HOME"] = "/home/brubble/.local/share"
    return os.environ["XDG_DATA_HOME"]


@pytest.fixture(scope="module")
def xdg_cache_home_env_var() -> pytest.fixture():
    os.environ["XDG_CACHE_HOME"] = "/home/brubble/.cache"
    return os.environ["XDG_CACHE_HOME"]


@pytest.fixture(scope="module")
def xdg_state_home_env_var() -> pytest.fixture():
    os.environ["XDG_STATE_HOME"] = "/home/brubble/.local/state"
    return os.environ["XDG_STATE_HOME"]


@pytest.fixture(scope="module")
def xdg_runtime_dir_env_var() -> pytest.fixture():
    os.environ["XDG_RUNTIME_DIR"] = "/var/run/user/9999"
    return os.environ["XDG_RUNTIME_DIR"]


@pytest.fixture
def xdg_base_dirs_with_env_vars_set(
    xdg_config_home_env_var,
    xdg_data_home_env_var,
    xdg_cache_home_env_var,
    xdg_state_home_env_var,
    xdg_runtime_dir_env_var,
) -> XDGBaseDirs:
    """
    Using Env Var Fixtures
    :return: XDGBaseDirs
    """
    # TODO: mock UID for all tests
    # mocker.patch("os.getuid", 9999)  # Spoof uid for tests
    input = XDGBaseDirs()
    return input


@pytest.fixture
def xdg_base_dirs_fixture():
    """
    Not Using Env Var Fixtures
    :return: None
    """
    input = XDGBaseDirs()
    return input
