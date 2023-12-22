import os
import locale
import configparser


class Settings:
    def __init__(self, config_file):
        self.config_file = os.path.abspath(os.path.join(os.path.dirname(__file__), config_file))
        # Check the existence of a file with settings
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"The configuration file '{self.config_file}' was not found")
        
        # Read the settings from the file
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)

        # Get the current system locale
        self.current_locale = locale.getlocale()[0]

    def get_opt(self, option):
        """Getting the value of the requested option from the settings file.

        Extract the desired configuration section depending on the current 
        locale and return the desired option
        """
        default_locale = 'en_EN'
        
        match self.current_locale:
            case locale_key if locale_key in self.config:
                locale_config = self.config[locale_key]
            case _:
                # If our system locale is not in the config, then we will use 
                # the local 'en_EN' from the settings file
                locale_config = self.config[default_locale]

        return locale_config.get(option)