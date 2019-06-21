import configparser


class MainConfig(object):
    def __init__(self, ini_path="./config/config.ini"):
        # singleton
        if not hasattr(self, "__instance"):
            self.read_config(ini_path)

    def read_config(self, ini_path):
        self.ini_path = ini_path
        self.__instance = configparser.ConfigParser()

        self.__instance.read(ini_path)
        MainConfig.__instance = self.__instance

    def __call__(self):
        return self.__instance


main_config = MainConfig()
