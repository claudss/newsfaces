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
                                filelist[0])
        image = io.imread(img_name)
        print ("IMG NAME: " + img_name)
        sample = {'image': image}
        if self.transform:
            sample = self.transform(sample)

        return sample
    
rootpath = 'aligned-faces-matlab/'
face_dataset = FaceData(root_dir=rootpath)

fig = plt.figure()
sample = face_dataset[0]

print(0, sample['image'].shape)

ax = plt.subplot(1, 1, 1)
plt.tight_layout()
ax.set_title('Sample #1')
ax.axis('off')
plt.show()