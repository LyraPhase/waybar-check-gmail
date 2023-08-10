import os
import pathlib
import sys

import git
import pytest

from waybar_check_gmail.util import XDGBaseDirs

# from pytest_mock import mocker


# Automatically mark tests by path below top-level 'tests' dir
def pytest_collection_modifyitems(config, items):
    # python 3.4/3.5 compat: rootdir = pathlib.Path(str(config.rootdir))
    rootdir = pathlib.Path(config.rootdir)
    for item in items:
        rel_path = pathlib.Path(item.fspath).relative_to(rootdir)
        mark_name = next((part for part in rel_path.parts if (part != "tests")), "")
        # mark_name = next((part for part in rel_path.parts), "")
        if mark_name:
            mark = getattr(pytest.mark, mark_name)
            item.add_marker(mark)


# Automatically configure pytest marks based on 'tests/' dir structure
def pytest_configure(config):
    rootdir = pathlib.Path(config.rootdir)
    repo = git.Repo(rootdir)
    # Get first subdir under rootdir matching "tests"
    _tests_dir = [_dir for _dir in rootdir.glob("tests")][0]
    # Get all first-level subdirs
    _tests_subdirs = [_subdir for _subdir in _tests_dir.glob("*") if (_subdir.is_dir())]
    _paths_considered = [
        d for d in _tests_subdirs if not str(d) in repo.ignored(_tests_subdirs)
    ]
    repo.close()
    # Create each subdir name as a pytest mark
    for _path in _paths_considered:
        mark_name = _path.stem
        config.addinivalue_line("markers", f"{mark_name}: {mark_name.capitalize()} tests")


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
