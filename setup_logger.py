#  Standard imports
import logging
import os
from datetime import datetime

if not os.path.exists("main.log"):
    open("main.log", 'x')

now = datetime.now()
date = now.strftime("%Y/%m/%d %A %I:%M:%S%p")

logging.basicConfig(filename="main.log", level=logging.INFO)
logger = logging.getLogger(' TIME: -{}- User'.format(date))
