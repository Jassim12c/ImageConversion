import os, sys
from PIL import Image

#  Image path
path = "images/image0.png"

#  Splitting image into path/name and format
f, e = os.path.splitext(path)

#  Combining path/name and the new format
output = f + ".jpeg"

#  Changing the format
os.rename(r'images\image0.png', r'{}'.format(output))
