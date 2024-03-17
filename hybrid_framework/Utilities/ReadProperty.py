import configparser

config_obj = configparser.RawConfigParser()
config_obj.read(r"C:\Users\user\PycharmProjects\pythonProject_WEMorning_dec\hybrid_framework\Configurations\config.ini")

class Read_Property:
    @staticmethod
    def GetURL():
        return config_obj.get('common data', 'url')

    @staticmethod
    def GetUsername():
        return config_obj.get('common data', 'username')

    @staticmethod
    def GetPassword():
        return config_obj.get('common data', 'password')