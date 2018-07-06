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
        print ("IMG NAME: " + img_name)
        sample = {'image': image}
        if self.transform:
            sample = self.transform(sample)
        return sample
    
    def __getpath__(self, idx):
        filelist = os.listdir(self.root_dir)
        filelist.sort()
        img_name = os.path.join(self.root_dir, filelist[idx])
        return img_name
    
    
class Crop(object):
    """Crop the images from our face data into desired dimensions

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

        top = np.random.randint(0, h - new_h)
        left = np.random.randint(0, w - new_w)

        image = image[top: top + new_h,
                      left: left + new_w]

        return {'image': image}
    
crop = Crop(125)

    
    
    
rootpath = 'aligned-faces-matlab/'
face_dataset = FaceData(root_dir=rootpath)

fig = plt.figure()

for i in range(len(face_dataset)):
    if i % 2 == 1:
        sample = face_dataset[i]
    
        print(i, sample['image'].shape)
    
        #ax = plt.subplot(1, 1, i + 1)
        plt.tight_layout()
        ax.set_title('Sample #{}'.format(i))
        img=mpimg.imread(face_dataset.__getpath__(i))
        imgplot = plt.imshow(img)
        ax.axis('off')
        plt.show()
        
    if i == 8:
        break
    

fig = plt.figure()
ax = plt.subplot(1, 1, 1)
sample = face_dataset[65]
cropped_sample = crop(sample)
img=mpimg.imread(face_dataset.__getpath__(65))
imgplot = plt.imshow(img)
plt.tight_layout()
ax.set_title(type(crop).__name__)
plt.show()

"""
sample = face_dataset[0]


print(0, sample['image'].shape)

ax = plt.subplot(1, 1, 1)
plt.tight_layout()
i = 1
ax.set_title('Sample #{}'.format(i))
img=mpimg.imread(face_dataset.__getpath__(i))
imgplot = plt.imshow(img)
ax.axis('off')
plt.show()



"""