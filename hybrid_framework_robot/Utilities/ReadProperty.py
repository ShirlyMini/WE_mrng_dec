import configparser
import rot_codec

config_obj = configparser.RawConfigParser()
config_obj.read(r"C:\Users\user\PycharmProjects\pythonProject_WEMorning_dec\hybrid_framework_robot\Configurations\config.ini")

class ReadProperty:
    @staticmethod
    def GetURL():
        return config_obj.get('common data', 'url')

    @staticmethod
    def GetUsername():
        return config_obj.get('common data', 'username')

    @staticmethod
    def GetPassword():
        pwsd_encoded = rot_codec.rot47_encode("admin")
        #pswd=config_obj.get('common data', 'password')
        return rot_codec.rot47_decode(pwsd_encoded)