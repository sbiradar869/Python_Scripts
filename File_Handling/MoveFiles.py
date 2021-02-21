import shutil
import os

source = 'F:/ASC/ASC_Source/'
destination = 'F:/ASC/ASC_Destination/'

files = os.listdir(source)

for f in files:
    #shutil.move(source+f, dest1)
    shutil.move(os.path.join(source, f), os.path.join(destination, f))
