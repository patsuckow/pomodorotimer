import os
import locale
import configparser


class Settings:
    def __init__(self, config_file):
        self.config_file = os.path.abspath(os.path.join(os.path.dirname(__file__), config_file))
        # Проверяем существование файла с настройками
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"The configuration file '{self.config_file}' was not found")
        
        # Читаем настройки из файла
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)

        # Получаем текущую локаль системы
        self.current_locale = locale.getlocale()[0]

    def get_opt(self, option):
        """Получение значения запрашиваемой опции из файла настроек.

        Извлекаем нужный раздел конфигурации в зависимости от текущей локали,
        и возвращаем нужную опцию
        """
        default_locale = 'en_EN'
        
        match self.current_locale:
            case locale_key if locale_key in self.config:
                locale_config = self.config[locale_key]
            case _:
                # Если нашей системной локали нет в конфиге, то будем использовать 
                # локаль 'en_EN' из файла настроек
                locale_config = self.config[default_locale]

        return locale_config.get(option)