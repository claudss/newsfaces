#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 14:09:40 2018

@author: Claudia Seidel

This code has been repurposed from PyTorch's data loading tutorial, found here:
https://pytorch.org/tutorials/beginner/data_loading_tutorial.html#dataset-class
"""
from __future__ import print_function, division
import os
import torch
import pandas as pd
from skimage import io, transform
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils

# Ignore warnings
import warnings
warnings.filterwarnings("ignore")

plt.ion()   # interactive mode



class FaceData(Dataset):
    """Face Landmarks dataset."""

    def __init__(self, root_dir, transform=None):
        """
        Args:
            self
            root_dir (string): path to directory with all face images
            transform (callable, optional): Optional transform to be applied
                on a sample.
        """
        self.root_dir = root_dir
        self.transform = transform

    def __len__(self):
        return len(os.listdir(self.root_dir))

    def __getitem__(self, idx):
        filelist = os.listdir(self.root_dir)
        filelist.sort()
        img_name = os.path.join(self.root_dir,
                                filelist[idx])
        image = io.imread(img_name)
        sample = {'image': image}
        if self.transform:
            sample = self.transform(sample)
        return sample
    
    def __getpath__(self, idx):
        filelist = os.listdir(self.root_dir)
        filelist.sort()
        img_name = os.path.join(self.root_dir, filelist[idx])
        return img_name

class CenterCrop(object):
    """Crops the image to the center/face region for better processing.

    Args:
        output_size (tuple or int): Desired output size. If int, square crop
            is made.
    """

    def __init__(self, output_size):
        assert isinstance(output_size, (int, tuple))
        if isinstance(output_size, int):
            self.output_size = (output_size, output_size)
        else:
            assert len(output_size) == 2
            self.output_size = output_size

    def __call__(self, sample):
        image = sample['image']

        h, w = image.shape[:2]
        new_h, new_w = self.output_size

        top = (h - new_h)//2
        left = (w - new_w)//2

        image = image[top: top + new_h,
                      left: left + new_w]

        return {'image': image}

rootpath = 'aligned-faces-matlab/'
face_dataset = FaceData(root_dir=rootpath)
crop = CenterCrop(275)

# simple for loop to crop all images
for i in range(len(face_dataset)):
    fig = plt.figure()
    sample = face_dataset[i]
    croppedsample = crop(sample)
    
    ax = plt.axes([0,0,1,1])
    plt.tight_layout()
    #ax.set_title(type(crop).__name__)
    ax.axis('off')
    plt.imshow(croppedsample['image'])
    plt.pause(0.001)
    #plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
    plt.show()
    
    fig.savefig('cropped/' + face_dataset.__getpath__(i)[20:], bbox_inches='tight', pad_inches=0, fix_aspect='false')
    


"""
# Attempt at using proper dataloading in pytorch to crop all images
crop = CenterCrop(275)
cropped = FaceData(root_dir=rootpath, transform=CenterCrop(275))
dataloader = DataLoader(cropped, batch_size=4,
                        shuffle=True, num_workers=4)


def show_batch(sample_batched):
    #Show image with landmarks for a batch of samples
    images_batch = sample_batched['image']
    batch_size = len(images_batch)
    im_size = images_batch.size(2)

    grid = utils.make_grid(images_batch)
    plt.imshow(grid.numpy().transpose((1, 2, 0)))


for ib, bsample in enumerate(dataloader):
    print(ib, bsample['image'].size())
    plt.figure()
    show_batch(bsample)
    #ax = plt.axes([0,0,1,1])
    #plt.tight_layout()
    #ax.set_title(type(crop).__name__)
    #ax.axis('off')
    #plt.imshow(dataloader['image'])
    #plt.pause(0.001)
    #plt.show()
    #fig.savefig('cropped/' + face_dataset.__getpath__(ib)[20:], bbox_inches='tight', pad_inches=0, fix_aspect='false')
"""