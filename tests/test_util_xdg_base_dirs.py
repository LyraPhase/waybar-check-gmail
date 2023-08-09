# import math
# import os

import pytest

# import pytest_mock


def test_xdg_config_home_env_defined(
    xdg_base_dirs_with_env_vars_set, xdg_config_home_env_var
):
    expected = xdg_config_home_env_var
    assert xdg_base_dirs_with_env_vars_set.xdg_config_home == expected


def test_xdg_data_home_env_defined(
    xdg_base_dirs_with_env_vars_set, xdg_data_home_env_var
):
    expected = xdg_data_home_env_var
    assert xdg_base_dirs_with_env_vars_set.xdg_data_home == expected


def test_xdg_cache_home_env_defined(
    xdg_base_dirs_with_env_vars_set, xdg_cache_home_env_var
):
    expected = xdg_cache_home_env_var
    assert xdg_base_dirs_with_env_vars_set.xdg_cache_home == expected


def test_xdg_state_home_env_defined(
    xdg_base_dirs_with_env_vars_set, xdg_state_home_env_var
):
    expected = xdg_state_home_env_var
    assert xdg_base_dirs_with_env_vars_set.xdg_state_home == expected


def test_xdg_runtime_dir_env_defined_and_exists(
    xdg_base_dirs_with_env_vars_set, xdg_runtime_dir_env_var, mocker
):
    mocker.patch("os.path.isdir", lambda _path: True)
    expected = xdg_runtime_dir_env_var
    assert xdg_base_dirs_with_env_vars_set.xdg_runtime_dir == expected


def test_xdg_runtime_dir_env_defined_but_does_not_exist_with_fallback(
    xdg_base_dirs_with_env_vars_set, xdg_runtime_dir_env_var, mocker
):
    xdg_base_dirs_with_env_vars_set.user_uid = 9999
    expected = "/run/user/9999"
    mocker.patch("os.path.isdir", lambda _path: True if _path == expected else False)
    assert xdg_base_dirs_with_env_vars_set.xdg_runtime_dir == expected


# TODO
# @pytest_mock.class_mocker.patch(tempfile.TemporaryDirectory, '__init__')
@pytest.mark.skip
def test_xdg_runtime_dir_env_defined_but_does_not_exist_with_last_resort_fallback(
    xdg_base_dirs_with_env_vars_set, xdg_runtime_dir_env_var, mocker
):
    # pytest_mock.class_mocker.patch(
    #     tempfile.TemporaryDirectory, "__init__"
    # )
    # mock_method.assert_called_with(
    #     prefix="waybar-check-gmail-",
    #     ignore_cleanup_errors=True
    # )
    xdg_base_dirs_with_env_vars_set.user_uid = 9999
    expected = "/run/user/9999"
    mocker.patch("os.path.isdir", lambda _path: True if _path == expected else False)
    assert xdg_base_dirs_with_env_vars_set.xdg_runtime_dir == expected


@pytest.mark.skip
def test_xdg_data_home():
    expected = "foo"
    assert "foo" == expected


@pytest.mark.skip
def test_xdg_cache_home():
    assert True


@pytest.mark.skip
def test_xdg_state_home():
    assert 1 == 1


@pytest.mark.skip
def test_xdg_runtime_dir():
    assert 2 == 2
