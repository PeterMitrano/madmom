
# coding: utf-8

# # Datset Visualization for Rhythmic Grouping
# 
# This notebook is scratch for investigating and visualizing our dataset(s)

# In[1]:

import numpy as np
import matplotlib.pyplot as plt
from util import show_playable_audio
import os


# In[11]:

base_dir = "study_v1.1_data/"
dataset = np.load(os.path.join(base_dir, "dataset/dataset.npz"))
sample_dir = os.path.join(base_dir, "samples")
x = dataset['x']
labels = dataset['labels']
sample_names = dataset['sample_names']

print(x.shape)
print(labels.shape)
print(sample_names.shape)


# The first dimension is the different samples. The second dimension is the time steps of each sample (which don't have to be the same but currently are). The $x$ matrix has a third dimension which are the features of each time step in each sample.

# In[12]:

def plot_features(i):
    plt.imshow(x[i].T)
    plt.title("Plot of features for {}".format(sample_names[i]))
    plt.tight_layout()
    plt.ylabel("features")
    plt.xlabel("time (frame idx)")
    plt.gca().get_yaxis().set_visible(False)    
    plt.show()
    
def plot_responses(i):
    plt.plot(labels[i])
    plt.show()


# In[17]:

sample_idx = 0
plot_features(sample_idx)
sample_path = os.path.join(sample_dir, sample_names[sample_idx])
show_playable_audio(sample_path)
plot_responses(sample_idx)

