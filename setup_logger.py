#  Standard imports
import logging
from datetime import datetime

now = datetime.now()
date = now.strftime("%Y/%m/%d %A %I:%M:%S%p")

logging.basicConfig(filename="main.log", level=logging.INFO)
logger = logging.getLogger(' TIME: -{}- User'.format(date))
