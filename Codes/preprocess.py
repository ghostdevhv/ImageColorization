import sys
import glob
import os
import numpy as np
import random
from PIL import Image

def createDataset(ImagesSet, flag):
	dirName = ""

	if(flag == False):
		file = open("../trainingImages.txt","w")
		if not os.path.exists("../trainingImages"):
			os.makedirs("../trainingImages")
		dirName = os.path.abspath("../trainingImages")

	if(flag == True):
		file = open("../testImages.txt","w")
		if not os.path.exists("../testImages"):
			os.makedirs("../testImages")
		dirName = os.path.abspath("../testImages")

	for image in ImagesSet:
		imageName = image.rsplit('/',1)[1]
		file.write(dirName+"/"+imageName+"\n")
		img = Image.open(image)
		img = img.resize((224,224), Image.ANTIALIAS)
		img.save(dirName+"/"+imageName)

	file.close()

def main(argv):
	folderPath = str(argv[0])
	absoluteFolderPath = os.path.abspath(folderPath)
	fileNames = glob.glob(absoluteFolderPath+"/*.jpg")
	random.shuffle(fileNames)
	trainingImagesSet = fileNames[0:20000]
	testingImagesSet = fileNames[20000:25000]

	createDataset(trainingImagesSet, flag = False)
	createDataset(testingImagesSet, flag = True)

if __name__ == '__main__':
	main(sys.argv[1:])