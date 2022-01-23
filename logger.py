import logging
import datetime
from pathlib import Path

class Logger:

    def __init__(self, name, debug):
        if debug:
            todaysDate = datetime.date.today().strftime("%Y-%m-%d")
            current_path = Path().absolute()
            logFile = Path(f"{str(current_path)}/configuration/logs/{name}_{todaysDate}.log")
            if logFile.is_file():
                logging.basicConfig(level=logging.DEBUG,
                                    format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
                                    datefmt="%m-%d %H:%M",
                                    filename=logFile)
            else:
                logging.basicConfig(level=logging.DEBUG,
                                    format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
                                    datefmt="%m-%d %H:%M",
                                    filename=logFile,
                                    filemode="w")
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)
        self.log = logging.getLogger(name)