# Datacompression-KIT
Development kit for users to quickly and easily develop his Visualisation or Analysis with default template, lib-programs, and examples.

[![N|](https://vuongblog.files.wordpress.com/2020/05/git_pt_vuong60.png)](https://vuongblog.wordpress.com)

# Install - Data prepare - Start 
## Install

- $ git clone https://github.com/tavuong/covid19-datakit.git
- $ cd ~/Datacompression-KIT
- $ pip install cv2
- $ pip install matplotlib
- $ pip install mumpy
- $ pip install panda, workbook,openpyxl

## Install with conda / Virtual Environment
- Installation_PC.md
- Installation_RPI.md

# Usage / Start:
$ python codecKIT-vuong.py

# Description

## Kit Stucture
- config.py: define for input / Output files
- codecKIT : frame work dashboard 
- lib :
    - block_process2 : block read, pocess and reconst
    - codec_dct      : demo  plug-in lib to block_procees: dvt_2, idct_2, lowpass_2d
## Data Structure
- input file is defined in config.py 
- output files are definde in config.py
- python codecKIT-vuong.py

- Input Block-length --> numberBlock
- Input 2D Lowpass length ---> nbit (Lowpass-example : Lowpass nbit * nbit of spectrals, rest set to o)
- blocks: ouput-folder with png-files for blocks

## modus P =Process        : Blocks generate, DCT and Idct to reconstruction:
                            - blocks/ images blocks (*.png)
                            - spect/  spect- blocks (*.png)
                            - filter/ filter- blocks (*.png)
                            - recon/  recon- blocks (*.png)
                            img_out / movieori.gif file of image blocks
                                      moviespect.gif file of spect blocks
                                      moviefilter.gif file of filter blocks
                                      movierecont.gif file of recont blocks
                                      spectNN.jpg  spec-blocks in ful-images
                                      filterNN.jpg  filter of spec-blocks in ful-images
                                      reconNN.jpg reconstruction images

## modus G= Blocks         : Blocks generate
                            - blocks/ images blocks (*.png)
                            img_out / movieori.gif file of blocks

## modus M= Mini Block in Image   : Blocks in big Image generate
                                - blocks/ images blocks (*.png) but mappinfg in big images
                                img_out / movieori-map.gif file of blocks

## WIKI
[Datacompresiion-KIT WIKI](https://github.com/tavuong/covid19-datakit/wiki) Info for using

## Examples: codecKIT-vuong.py

- In Git: Example  for datacompression by 64*64 Image, block: 16*16, lowpass_Filter 4*4
- In Git for Entwickler: dont push your processed Data to GIT

# Project : Datacompression-KIT
Development kit for Datacompression to quickly and easily develop his Visualisation or Analysis with default template, lib-programs, and examples.

[![N|](https://vuongblog.files.wordpress.com/2020/05/git_pt_vuong60.png)](https://vuongblog.wordpress.com)

Initiator: Dr.-Ing. The Anh Vuong (admin)
Entwickler Team: Dr. The Anh Vuong, Tim Rosenkranz

License: MIT
