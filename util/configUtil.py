import sys
import json
import logging


class MainConfig(object):
    def __init__(self, ini_path="./config/config.json"):
        # singleton
        if not hasattr(self, "__instance"):
            self.read_config(ini_path)

    def read_config(self, ini_path):
        self.ini_path = ini_path
        str_result = open(self.ini_path, "r").read()
        try:
            self.__instance = json.loads(str_result)
            self.check_config()
        except Exception as e:
            logging.error(u"config file:%s broken, please re generate the config file" % (self.ini_path, ))
            sys.exit()

        MainConfig.__instance = self.__instance

    def __call__(self):
        return self.__instance

    def check_config(self):
        return True


main_config = MainConfig()
