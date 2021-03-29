# Process_2D.py
# Object oriented - 2D Processing
# Datum : 29.03.2021
# Author Dr.-Ing. The Anh Vuong 
import cv2  # openCV
import config
from lib.codec_dct import *
class Block2D:
  def __init__(self, block, blockname):
    self.block = block
    self.name = blockname

  def print(self):
#	  print (self.block)
	  print("Hello my name is " + self.name)

  def save_image(self,nf):
#	  print("Filename is " + self.name)
	  filename= self.name + str(nf)+ '.png'
	  cv2.imwrite(filename,self.block)

  def save_image_jpg(self,nf):
#	  print("Filename is " + self.name)
	  filename= self.name + str(nf)+ '.jpg'
	  cv2.imwrite(filename,self.block)

  def copy_block(self):
	  return (self.block)

  def refill(self,miniblock,nbI,nbI1,nbK,nbK1):
	  for i in range (nbI, nbI1):
		  for k in range (nbK, nbK1):
			  self.block[i][k]=miniblock[i-nbI][k-nbK]
#	  return (self.block)

  def dct_2D(self):
	  return dct_2 (self.block)
  def idct_2D(self):
	  return idct_2 (self.block)
  def lowpass_2D(self,nbit):
	  return lowpass_2d (self.block,nbit)

