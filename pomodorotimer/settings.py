import os
import locale
import configparser


class Settings:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.load_config()

    def load_config(self):
        config_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "config.ini"))
        # Check the existence of the configuration file
        if not os.path.isfile(config_file):
            raise FileNotFoundError(f"Configuration file '{config_file}'not found.")
        # Read the settings from the file using the ConfigParser() class method
        self.config.read(config_file)

    def get_locale(self) -> str:
        """Get a localized configuration from the settings file."""
        # Get the current system locale
        current_locale = locale.getlocale()[0]
        if current_locale in self.config:
            return current_locale
        else:
            return 'en_EN'
    
    def get_setting(self, option):
        """Get the string values of the requested option from the settings file."""
        # If the resulting line is '\\n', then first replacing it with '\n'
        return self.config.get(self.get_locale(), option).replace('\\n', '\n')