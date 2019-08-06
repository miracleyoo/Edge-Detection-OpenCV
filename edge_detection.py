#!/usr/bin/env python
#coding=utf-8

import cv2
import os
import numpy as np  
import argparse
from time import time

def main():
    if opt.inverse:
        print("==> Mission start! You choosed black background and white line version.")
    else:
        print("==> Mission start! You choosed white background and black line version.")
    if os.path.isdir(opt.path):
        outdir = os.path.join(opt.path, 'edge_det')
        filelist = [os.path.join(opt.path, i) for i in os.listdir(opt.path) if not (i.startswith('.') or os.path.isdir(os.path.join(opt.path, i)))]
    else:
        outdir = os.path.join(os.path.split(opt.path)[0],'edge_det')
        filelist = [opt.path]
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    for afile in filelist:
        process(afile, outdir)

def process(imgpath, outdir):
    sta = time()
    img = cv2.imread(imgpath, 0)
    img = cv2.GaussianBlur(img,(3,3),0)
    canny = cv2.Canny(img, 50, 150)
    outname = os.path.join(outdir, os.path.split(imgpath)[1])
    if opt.inverse:
        cv2.imwrite(outname ,canny)
    else:
        cv2.imwrite(outname ,cv2.bitwise_not(canny))
    print("==> Image:",os.path.split(imgpath)[1],'successfully processed!\t Time:', str(time()-sta),'s')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default='~/Documents/图片/Anime_pic', help='The path of a file or a folder you want to detect the edge.')
    parser.add_argument('--inverse', action="store_true", default=False)
    opt = parser.parse_args()
    opt.path = os.path.expanduser(opt.path)
    main()