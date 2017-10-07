
# coding: utf-8

# # Datset Visualization for Rhythmic Grouping
# 
# This notebook is scratch for investigating and visualizing our dataset(s)

# In[1]:

import numpy as np
import matplotlib.pyplot as plt
from util import show_playable_audio
import os


# In[2]:

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

# In[62]:

def plot_features_and_labels(i):
    fig = plt.figure(figsize=(20,10))
    feature_ax = plt.subplot(211)
    feature_ax.imshow(x[i].T, interpolation='nearest', aspect='auto')
    feature_ax.set_ylabel("features")
    feature_ax.set_xlabel("time (frame idx)")
    feature_ax.get_yaxis().set_visible(False)
    feature_ax.set_title("features for {}".format(sample_names[i]))
    
    label_ax = plt.subplot(212, sharex=feature_ax)
    label_ax.bar(range(len(labels[i])), labels[i])
    label_ax.set_title("probability of grouping")
    
    plt.tight_layout()
    plt.show()


# In[73]:

sample_idx = 0
plot_features_and_labels(sample_idx)
sample_path = os.path.join(sample_dir, sample_names[sample_idx])
show_playable_audio(sample_path)


# In[78]:

print("Percent of frames with non-zero labels: {}%".format(np.count_nonzero(labels) / labels.size))
print("Total responses: {}".format(labels.size))


# In[ ]:



