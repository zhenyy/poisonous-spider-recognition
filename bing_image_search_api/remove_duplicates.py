import hashlib
import os
import matplotlib.pyplot as plt
import time
import numpy as np
from hashlib import md5
from imageio import imread

#%% 
def file_hash(filepath):
    """
    Function that returns a hash of a file
  
    Parameters: 
    filepath: string of a file path 
  
    Returns: 
    string: file hash 
    """
    with open(filepath, 'rb') as f:
        return md5(f.read()).hexdigest()

#%%
def remove_duplicates():
    """
    Function that loops through the images in a folder 
    and remove duplicates
    """

    duplicates = []
    hash_keys = {}

    files_list = os.listdir()

    for index, filename in enumerate(files_list):
        if os.path.isfile(filename):
            filehash = file_hash(filename)
        if filehash not in hash_keys.keys(): # a novel image
            hash_keys[filehash] = index
        else:  # a duplicate image
            duplicates.append((index, hash_keys[filehash]))

    # remove duplicate images by their paths
    for index, _ in duplicates:
        os.remove(files_list[index])