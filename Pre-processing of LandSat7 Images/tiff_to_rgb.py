from libtiff import TIFF
import sys
import numpy as np
import os
from PIL import Image
from os import listdir
from os.path import isfile, join
import pickle
import h5py
import scipy.misc
import subprocess


inputFolder = sys.argv[1]
outputFolder = inputFolder+"_outfiles"
#os.makedirs(outputFolder, exist_ok=True)
if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)
    
onlyfiles = [f for f in listdir(inputFolder) if isfile(join(inputFolder, f))]


for currImageName in onlyfiles:
	
	destImageName=currImageName[:-4]+'.jpeg'
	print(currImageName)
	print(destImageName)
	cmd ='gdal_translate --config GDAL_PAM_ENABLED NO -of JPEG -co QUALITY=100 -ot Byte -a_nodata 0 -scale 0 2750 1 255 -b 1 -b 2 -b 3 -of JPEG ' + inputFolder+'/'+currImageName  +'  '+  outputFolder+'/'+ destImageName
	print (cmd)
	subprocess.call(cmd , shell=True)

	




