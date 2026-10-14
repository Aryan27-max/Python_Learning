# logging - a better version of print() for keeping track of what your program does.
# You get levels, timestamps, and you can send it to a file.

import logging

# basicConfig sets things up. By default only WARNING and above are shown,
# so we lower the level to DEBUG to see everything.
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)

# The five levels, from least to most serious
logging.debug("debug: tiny details for fixing bugs")
logging.info("info: things are working as expected")
logging.warning("warning: something looks a bit off")
logging.error("error: something failed")
logging.critical("critical: the program might not survive this")

# In bigger projects, give each file its own logger
logger = logging.getLogger(__name__)
logger.info("hello from my own logger")

# Log the full error details while catching an exception
try:
    numbers = [1, 2]
    numbers[5]
except IndexError:
    logging.error("Something went wrong", exc_info=True)

# Want it in a file too? Add a file handler
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.WARNING)
logger.addHandler(file_handler)
logger.warning("this one also goes into app.log")
