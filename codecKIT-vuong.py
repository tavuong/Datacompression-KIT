# CodecKIT.py
# Frame Work für block-codierung 
# Status: Entwicklung
# Berechen Codierung eines Bilders aus JPEG mit OPencv
# Der Vorgang wird analyse
# Die Spektrum wird als Jpeg-Bilde rerzeugt!
# Die Matrix des Spektrum wird:
# - direckt in der Rechnung von Oroiginal -> Spectrum
# - indirect aus der reconstruierte Bild 
# Developer: Dr. -Ing. The Anh Vuong

# -*- coding: utf-8 -*-

import cv2  # openCV
from config import *
from lib.bloc_process2 import *
from lib.bloc_process import *
from lib.live_process import *
from lib.imgRW import *
from lib.dct import *
from lib.idct import *
from math import cos, pi, sqrt
import numpy as np
import matplotlib.pylab as plt
import sys


# Parameter reading
# Input Bilder BGR statt RGB
numberModus = input("modus (P=Process, G=Blocks, M=BlockinImage, V=video, I=ImageCapture): ") 
# for test param is set to 1
# param = input ("Blockstoring? Yes=1 / no =0: ") 
# param = int (param)
param = 1

# Video Processing (in develop)
if (numberModus in "V"):
    print('*************** Live Cam  processing ****************')
    icall = camera_CODEC (param)
    sys.exit(0)

if (numberModus in "I"):
    print('*************** ImageClick processing ****************')
    icall = image_Click (param)
    sys.exit(0)

# Image Processing 
# Input Parameter 

numberBlock = input("Blocklength: ") 
numberBlock = int(numberBlock)
numberCoefficients = numberBlock * numberBlock

if (numberModus == "P"):
    nbit = input ("2D LowpassFilter-Blocklength:")
    nbit = int (nbit)
else:
    nbit = numberBlock

print("image_input " + config.imageToRead + " !" + "\n")
print("Blocklength: " + str(numberBlock) + " !" + "\n")
print("Number of DCT-coefficients: " + str(numberCoefficients) + " !" + "\n")
print("2D LowpassFilter- Blocklength: " + str(nbit) + " !" + "\n")
rcontinue = input  ("is setting correct (y /n)? ")
if (rcontinue == "n") : sys.exit(0)

print('*************** Input Datein lesen ****************')
img = imgC2G(config.imageToRead,config.imageGray,1)   
nb = numberBlock
height = img.shape[0]
width = img.shape[1]
print("pic height:" + str(height))
print("pic width:" + str(width))

print('*************** Blockdatei processing ****************')
# Mini Blocks generator 
#	from lib.blockprocess import imgBLOCK1 
#-------------------------------------
#	os.mkdir("blocks/")
if (numberModus in "G"):
    a = np.arange(0,numberCoefficients)
    b = a.reshape(numberBlock,numberBlock)
    img2 = np.zeros_like(b).astype(int)
    imgBLOCK = imgBLOCK1(img, img2, numberBlock, param)
    animator_call = animator(config.dirBlocks,"ori-blocks")

#-------------------------------------
# Blocks im Bild
# from lib.imgRW import imgSORT
# imgBLOCK = imgSORT(img, numberBlock, 2)  
if (numberModus in "M"):
    imgBLOCK = imgBlockinImage(img, numberBlock, param)
    animator_call = animator(config.dirBlocks,"ori-map")

#-------------------------------------
# Blocks generator
# dct  -> Spect- blocks
# odct -> reconstr -blocks 
# blocks --> Big image back
# from lib.blockprocess import imgBLOCK1 
#-------------------------------------

if (numberModus in "P"):
    a = np.arange(0,numberCoefficients)
    b = a.reshape(numberBlock,numberBlock)
    img2 = np.zeros_like(b).astype(float)
    imgBLOCK = imgBLOCK2(img, img2, numberBlock, param,nbit)
    print('*************** output ./img_out/movie*.gif ***********')
    if (param == 1):
        print ('wait ...')        
        animator_call = animator(config.dirBlocks,"ori")
        animator_call = animator(config.dirSpect,"spect")
        animator_call = animator(config.dirFilter,"filter")
        animator_call = animator(config.dirRecon,"recon")
# show option
#        ishow= imgSHOW2(numberBlock)
        print ('result show! To exit close picture!') 
        plt.show() 
