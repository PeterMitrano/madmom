
# coding: utf-8

# # Datset Visualization for Rhythmic Grouping
# 
# This notebook is scratch for investigating and visualizing our dataset(s)

# In[1]:

import numpy as np
import matplotlib.pyplot as plt


# In[2]:

dataset = np.load("../data/study_v1.1_data/dataset/dataset.npz")
x = dataset['x']
labels = dataset['labels']
sample_names = dataset['sample_names']

print(x.shape)
print(labels.shape)
print(sample_names.shape)


# The first dimension is the different samples. The second dimension is the time steps of each sample (which don't have to be the same but currently are). The $x$ matrix has a third dimension which are the features of each time step in each sample.

# In[18]:

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


# In[19]:

plot_features(4)
plot_responses(4)


# In[23]:

plot_features(7)
plot_responses(7)


# In[ ]:



