import os
import tempfile

from .util import warn


class XDGBaseDirs:
    """
    XDGBaseDirs provides default directories according
    to freedesktop.org XDG Base Directories Standard
    """

    def __init__(self):
        self.user_uid = os.getuid()
        # Initialize default values.
        print("XDG_CONFIG_HOME=%s" % os.getenv("XDG_CONFIG_HOME", None))
        self.xdg_config_home = os.getenv(
            "XDG_CONFIG_HOME", os.path.expanduser("~/.config")
        )
        self.xdg_data_home = os.getenv(
            "XDG_DATA_HOME", os.path.expanduser("~/.local/share")
        )
        self.xdg_cache_home = os.getenv("XDG_CACHE_HOME", os.path.expanduser("~/.cache"))
        self.xdg_state_home = os.getenv(
            "XDG_STATE_HOME", os.path.expanduser("~/.local/state")
        )

    @property
    def xdg_runtime_dir(self):
        _xdg_runtime_dir = os.getenv(
            "XDG_RUNTIME_DIR",
            os.path.join(os.path.expanduser("/var/run/user"), str(self.user_uid)),
        )
        if not os.path.isdir(_xdg_runtime_dir):
            _xdg_runtime_fallback = os.path.join("/run/user", str(self.user_uid))
            warn("XDG_RUNTIME_DIR (%s) does not exist!" % _xdg_runtime_dir)
            warn("Attempting fallback to: %s" % _xdg_runtime_fallback)
            if not os.path.isdir(_xdg_runtime_fallback):
                warn(
                    "Fallback XDG_RUNTIME_DIR (%s) does not exist!"
                    % _xdg_runtime_fallback
                )
                self.xdg_runtime_last_resort_fallback = tempfile.TemporaryDirectory(
                    prefix="waybar-check-gmail-", ignore_cleanup_errors=True
                )
                _xdg_runtime_dir = self.xdg_runtime_last_resort_fallback.name

                warn("Last resort fallback to: %s" % _xdg_runtime_dir)
            else:
                _xdg_runtime_dir = _xdg_runtime_fallback
        return _xdg_runtime_dir

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val:
            warn(
                "Exception %s(%s) encountered within XDG_RUNTIME_DIR '%s' context",
                exc_type,
                exc_val,
                self.xdg_runtime_dir,
            )
            warn("Traceback: %s" % exc_tb)
        if self.xdg_runtime_last_resort_fallback:
            self.xdg_runtime_last_resort_fallback.cleanup()

    def __repr__(self):
        return (
            "%s(xdg_config_home=%s, xdg_data_home=%s, xdg_cache_home=%s,"
            "xdg_state_home=%s, xdg_runtime_dir=%s)" % self.__class__.__name__,
            self.xdg_config_home,
            self.xdg_data_home,
            self.xdg_cache_home,
            self.xdg_state_home,
            self.xdg_runtime_dir,
        )
