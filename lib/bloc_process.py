import cv2  # openCV
import config
from PIL import Image 
from math import cos, pi, sqrt
import numpy as np
import os
import imageio

def imgBLOCK1(img, img2, numberBlock=0, param=0):
	
	
#	print(img1.shape)

	nb = numberBlock
	para = param
	height = img.shape[0]
	width = img.shape[1]
	nzahl = int(height / nb)
#	print("pic height:" + str(height))
#	print("pic width:" + str(width))
#	print("block:" + str(nb))
#	print("Param:" + str(para))
#   --------------------------------- 
#   preset ordner 
#	os.mkdir("./blocks/")		
	imageBlock = np.zeros_like(img2).astype(int)
	nf = 0
	nbK=0
	nbK1=nb
	nbI=0
	nbI1=nb
	for ri in range (nzahl):
		for r in range (nzahl):
			for i in range (nbI, nbI1):
				for k in range (nbK, nbK1):
					imageBlock[i-nbI][k-nbK]= img[i][k]
			print ("Block calculated "+ str(nf) + "\r")
			cv2.imwrite(config.dirBlocks + '/block' + str(nf)+ '.png',imageBlock)
			nf = nf  +1
#			imageBlock = np.zeros_like(img).astype(int)
			nbK = nbK + nb
			nbK1= nbK1 + nb
		nbI = nbI + nb
		nbI1= nbI1 + nb
		nbK=0
		nbK1=nb	
	return imageBlock
#-----------------------------------------------------------------------
def imgBlockinImage(img, numberBlock=0, param=0):
	
#	param = 0 : komplet image stored
#   param = 1 : block-spechts- reconst stored 

	nb = numberBlock
	para = param
	height = img.shape[0]
	width = img.shape[1]
	nzahl = int(height / nb)
#	print("pic height:" + str(height))
#	print("pic width:" + str(width))
#	print("block:" + str(nb))
#	print("Param:" + str(para))
#   --------------------------------- 
#   preset ordner 
#	os.mkdir("./blocks/")		
	imageBlock = np.zeros_like(img).astype(int)
	nf = 0
	nbK=0
	nbK1=nb
	nbI=0
	nbI1=nb
	
	for ri in range (nzahl):
		for r in range (nzahl):
			for i in range (nbI, nbI1):
				for k in range (nbK, nbK1):
					imageBlock[i][k]= img[i][k]
			print ("Block calculated "+ str(nf) + "\r")
			cv2.imwrite(config.dirBlocks +'/block' + str(nf)+ '.png',imageBlock)
			nf = nf  +1
			imageBlock = np.zeros_like(img).astype(int)
			nbK = nbK + nb
			nbK1= nbK1 + nb
		nbI = nbI + nb
		nbI1= nbI1 + nb
		nbK=0
		nbK1=nb	
	return imageBlock
