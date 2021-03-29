# bloc_process2.py
# - Image serialize in mini blocks
# - Pipe structure for  Processing
# - Refill miniblocks to images 
# Datum : 29.03.2021
# Author Dr.-Ing. The Anh Vuong 
import cv2  # openCV
import config
from lib.codec_dct import *
from lib.imgRW import *
from lib.Process_2D import *
#from lib.dct import dct_2d, dct_1d
#from lib.idct import idct_2d, idct_1d 
from PIL import Image 
from math import cos, pi, sqrt
import numpy as np
import matplotlib.pylab as plt
# from scipy import fftpack
import os
import imageio

def imgBLOCK2(img, img2, numberBlock=0, param=0, nbit=0):
	
	
#	param = 0 : komplet image stored
#   param = 1 : block-spechts- reconst stored 
	nb = numberBlock
	para = param
	nmap = nbit
	height = img.shape[0]
	width = img.shape[1]
	nzahl = int(height / nb)
#	print("pic height:" + str(height))
#	print("pic width:" + str(width))
#	print("block:" + str(nb))
#	print("Param:" + str(para))
#   ------------ Preset Mini-Block --------------------- 
#   preset ordner 
#	os.mkdir("./blocks/")		
	imageBlock = np.zeros_like(img2).astype(float)
#	imageSpect = np.zeros_like(img2).astype(float)
#	imageFilter = np.zeros_like(img2).astype(float)
#	imageRecon = np.zeros_like(img2).astype(float)
#   ------------ Preset full-Image ---------------
	imgReconful = np.zeros_like(img).astype(float)
	imgSpectful = np.zeros_like(img).astype(float)
	imgFilterful = np.zeros_like(img).astype(float)

#   Preset full-image
#	filename_save = config.dirImgout + '/test-'
#	ps = Block2D(img,filename_save)
#	imgReconful2 = ps.copy_block()
#	precont1 = Block2D(imgReconful2,filename_save)
#	precont1.save_image(2000)	

	filename_save = config.dirImgout + '/spect-'
	pspect = Block2D(imgSpectful,filename_save)

	filename_save = config.dirImgout + '/filter-'
	pfilter = Block2D(imgFilterful,filename_save)

	filename_save = config.dirImgout + '/reconst-'
	precont = Block2D(imgReconful,filename_save)

	ncof = 0
	ncof = int(nb * nb)
	nf = 0
	nbK=0
	nbK1=nb
	nbI=0
	nbI1=nb
#   ------------ Pipe Processing --------------------- 
#
# Blockweise processing implimented
# ORI >>> DCT >>> FILTER >>> IDCT >>> RECONST

	for ri in range (nzahl):
		for r in range (nzahl):
#-----------------ORI -------------
			for i in range (nbI, nbI1):
				for k in range (nbK, nbK1):
					imageBlock[i-nbI][k-nbK]= img[i][k]
			print ("Block calculated "+ str(nf) + "\r")
			filename_save = config.dirBlocks + '/block' 
			ps = Block2D(imageBlock,filename_save)
			ps.save_image(nf)	
#-----------------Spectrum  -------------
			imageSpect= ps.dct_2D ()
			filename_save = config.dirSpect + '/spect' 
			ps = Block2D(imageSpect,filename_save)
			ps.save_image(nf)	

#-----------------2D-Filter  -------------
			imageFilter= ps.lowpass_2D(nmap)
			filename_save = config.dirFilter + '/filter' 
			ps = Block2D(imageFilter,filename_save)
			ps.save_image(nf)	

#-----------------IDCT   -------------
			imageRecont= ps.idct_2D ()
			filename_save = config.dirRecon + '/recon' 
			ps = Block2D(imageRecont,filename_save)
			ps.save_image(nf)

#---nf = Block index 
			nf = nf  +1
#--------------------Block Fill to Image -----------------------------
#			for i in range (nbI, nbI1):
#				for k in range (nbK, nbK1):
#					imgReconful[i][k]=imageRecont[i-nbI][k-nbK]
#					imgSpectful[i][k]=imageSpect[i-nbI][k-nbK]
#					imgFilterful[i][k]=imageFilter[i-nbI][k-nbK]

			pspect.refill (imageSpect,nbI,nbI1,nbK,nbK1)
			pfilter.refill (imageFilter,nbI,nbI1,nbK,nbK1)
			precont.refill (imageRecont,nbI,nbI1,nbK,nbK1)
#			precont1.refill (imageFilter,nbI,nbI1,nbK,nbK1)
			nbK = nbK + nb
			nbK1= nbK1 + nb
		nbI = nbI + nb
		nbI1= nbI1 + nb
		nbK=0
		nbK1=nb	
#	cv2.imwrite(config.dirImgout + '/spect-' + str(nf)+ '.jpg',imgSpectful)
#	cv2.imwrite(config.dirImgout + '/filter-' + str(nf)+ '.jpg',imgFilterful)
#	cv2.imwrite(config.dirImgout + '/reconst-' + str(nf)+ '.jpg',imgReconful)

#	precont1.save_image(100)

# ---- Save full immages

	filename_save = config.dirImgout + '/spect-'
	ps = Block2D(imgSpectful,filename_save)
	ps.save_image_jpg(nf)

	filename_save = config.dirImgout + '/filter-'
	ps = Block2D(imgFilterful,filename_save)
	ps.save_image_jpg(nf)

	filename_save = config.dirImgout + '/reconst-'
	ps = Block2D(imgReconful,filename_save)
	ps.save_image_jpg(nf)


	ishow= imgSHOW2(nf)
	return imageBlock