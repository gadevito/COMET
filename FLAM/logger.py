import logging
import os
import sys

def _init_logger():
    os.makedirs("./logs", exist_ok=True)
    #logging.basicConfig(level=logging.DEBUG, format=f"%(levelname)-8s: \t %(filename)s %(funcName)s %(lineno) - %(message)s")
    logger = logging.getLogger("COSMIC_ANALYSIS")
    logger.setLevel(logging.DEBUG)
    logger_formatter = logging.Formatter("[%(name)s: %(asctime)s] {%(lineno)d} %(levelname)s - %(message)s", "%m-%d %H:%M:%S")
    fileHandler = logging.FileHandler(filename="./logs/analysis.log",)
    fileHandler.setFormatter(logger_formatter)
    fileHandler.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(stream=sys.stdout)
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(logger_formatter)
        
    logger.addHandler(ch)
    logger.addHandler(fileHandler)

_init_logger()
_logger = logging.getLogger("COSMIC_ANALYSIS")