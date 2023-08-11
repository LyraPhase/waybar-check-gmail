import configparser
from typing import TYPE_CHECKING

from util import die

if TYPE_CHECKING:
    # from collections.abc import Iterable
    from typing import Dict, Union

    from typeshed import AnyPath

    # from typing import List, Set, Dict, Tuple
else:
    AnyPath = None


class Config:
    _map: Dict[str, Dict[str, Union[str, bool, None]]] = {}

    def __init__(self, fn: AnyPath):
        self._map = {
            "Auth": {
                "Password": None,
                "PasswordCommand": None,
                "Username": None,
            },
            "CustomHeaders": {},
            "General": {
                "AuthMethod": "basic",
                "Debug": False,
                "DryRun": True,
                "HTTPS": True,
                "Hostname": None,
                "InsecureSSL": False,
                "Path": None,
                "Verbose": False,
            },
            "OAuth2": {
                "ClientID": None,
                "ClientSecret": None,
                "RedirectURI": "http://127.0.0.1",
                "Scope": None,
            },
        }
        self.verbose = self.get("General", "Verbose")

        config = configparser.RawConfigParser()
        # TODO: Why did calcurse-caldav set this function to str?  MyPy + Flake8 say it's
        # a syntax error
        # config.optionxform = str
        # TODO: Figure out precedence between --verbose arg parse and Config.verbose
        #       Maybe reimplement this as YAML instead
        if self.verbose:
            print("Loading configuration from " + fn + " ...")
        try:
            config.read_file(open(fn))
        except FileNotFoundError:
            die("Configuration file not found: {}".format(fn))

        for sec in config.sections():
            if sec not in self._map:
                die("Unexpected config section: {}".format(sec))

            if not self._map[sec]:
                # Import section with custom key-value pairs.
                self._map[sec] = dict(config.items(sec))
                continue

            # Import section with predefined keys.
            for key, val in config.items(sec):
                if key not in self._map[sec]:
                    die("Unexpected config key in section {}: {}".format(sec, key))
                if self._map[sec][key] is bool:
                    self._map[sec][key] = config.getboolean(sec, key)
                else:
                    self._map[sec][key] = val

    def section(self, section):
        return self._map[section]

    def get(self, section, key):
        return self._map[section][key]
