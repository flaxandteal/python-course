# -*- coding: utf-8 -*-
"""
Configuration utilities for ensuring consistent, settable behaviour.

@author: philtweir
"""

import os
from pkg_resources import Requirement, resource_filename

import appdirs
import yaml

from . import PACKAGE_NAME, PACKAGE_AUTHOR

DEFAULT_CONFIG_FILE = 'latency.yaml'

class ConfigManager:
    """
    Manages the configuration loading
    """

    _config = None
    _config_filename = None

    def get(self, config_filename):
        """
        Return the configuration object, reloading only if necessary
        """

        if not self._config or config_filename != self._config_filename:
            self.load(config_filename)

        return self._config

    def load(self, config_filename):
        """
        Load or re-load the configuration from the given file
        """

        with open(config_filename, 'r') as config_file:
            config = yaml.safe_load(config_file)

        # perhaps any other modifications to config happen here (e.g. interpolation)

        self._config_filename = config_filename
        self._config = config

def find_config_file():
    """
    Search for the default configuration file.
    """
    # Strictly, this approach has disadvantages, as it
    # does not make any guarantees about race-conditions or
    # presence of a while when it's actually opened.
    # However, given the context, this sequential approach is
    # arguably clearer.

    filename = DEFAULT_CONFIG_FILE

    # If the config file is present where we are running,
    # load it - this provides an intuitive way of overriding
    # installed config.
    if os.path.exists(filename):
        return filename

    # A good second attempt is to use the XDG Base Directory
    # Specification - that is, ~/.config/<packagename>
    # This makes it easy for a user to override for themselves.
    user_dir = appdirs.user_data_dir(PACKAGE_NAME, PACKAGE_AUTHOR)
    user_dir_filename = os.path.join(user_dir, DEFAULT_CONFIG_FILE)
    if os.path.exists(user_dir_filename):
        return user_dir_filename

    package_filename = resource_filename(Requirement.parse(PACKAGE_NAME), DEFAULT_CONFIG_FILE)
    if os.path.exists(package_filename):
        return package_filename

    # Re-using built-in exceptions, as long as they make semantic sense, is reasonable.
    raise FileNotFoundError(f"Could not find configuration file: {DEFAULT_CONFIG_FILE}")


def get_config(config_filename=None):
    """
    Retrieve or load the config from the given file.
    """

    if config_filename is None:
        config_filename = find_config_file()

    return _config_manager.get(config_filename)

_config_manager = ConfigManager()
