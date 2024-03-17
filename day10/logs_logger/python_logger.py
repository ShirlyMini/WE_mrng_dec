import logging
import os

# debug(1)--infor(2)--warning(3-default)---error(4)--critcal(5)
# log_handler=logging.getLogger()
# log_handler.setLevel(logging.DEBUG)
# print(logging.getLogger())
# log_handler=logging.getLogger()
# log_handler.setLevel(logging.DEBUG)
# print(log_handler)
location = fr'{os.getcwd()}\test_log.txt'
# logging.basicConfig(filename=location,
#                     filemode='a',level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s %(module)s',
#                     force=True)
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s %(module)s',
#                     force=True)
# stream_handler = logging.StreamHandler()
logging.basicConfig(handlers=[logging.FileHandler(filename=location, mode="a"), logging.StreamHandler()],
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s %(module)s',
                    force=True)

logging.debug("this is debug level")
logging.info("this is info level")
logging.warning("this is warn level")
logging.error("this is info level")
logging.critical("this is critical level")