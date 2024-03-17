import logging
import datetime
td1 = datetime.datetime.now()
date = td1.strftime('%Y%b%d%H%M%S')


def custom_logging():
    location=fr".\Logs\log{date}.txt"
    logging.basicConfig(handlers=[logging.FileHandler(filename=location, mode="w"), logging.StreamHandler()],
                        level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(message)s %(module)s',
                        force=True)
    return logging