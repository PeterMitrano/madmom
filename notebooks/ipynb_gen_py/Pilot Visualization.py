
# coding: utf-8

# # Pilot Data Visualization

# In[1]:

import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import glob
from matplotlib import animation, rc
from IPython.display import HTML

from util import show_playable_audio


# In[2]:

root = "study_v2.23_data/"
data_directory = os.path.join(root, "pilot_responses")
samples_directory = os.path.join(root, "samples")

csv_files = glob.glob(os.path.join(data_directory, "*.csv"))

samples_to_responses = {}
samples = []
for csv_file in csv_files:
    subject = os.path.split(csv_file)[-1]
    reader = csv.reader(open(csv_file, 'r'))
    for line in reader:
        data = line[1][:-1]
        split_data = data.split(" ")
        sample_name = split_data[1]
        sample_path = os.path.join(samples_directory, sample_name)
        sample = {'name': sample_name, 'path:': sample_path}
        responses = [float(t) for t in split_data[3:]]
        if sample_name not in samples_to_responses:
            samples_to_responses[sample_name] = {'length': float(split_data[2]), 'path': sample_path, 'subjects': {}}
            samples.append(sample_name)
        
        if subject not in samples_to_responses[sample_name]['subjects']:
            samples_to_responses[sample_name]['subjects'][subject] = {'responses': []}
            
        samples_to_responses[sample_name]['subjects'][subject]['responses'].append(responses)
        


# In[3]:

print(samples)


# In[21]:

test_sample = '09_AcousticGtr2.mp3'
sample_data = samples_to_responses[test_sample]
subjects = sample_data['subjects']
length = int(sample_data['length'])
bins = length//200
show_playable_audio(sample_data['path'])

fig, ax = plt.subplots()
ax.set_xlim((0, length))
ax.set_ylim((0, 1))

plt.title(sample_name)
plt.xlabel("milliseconds")
cursor, = ax.plot([], [], lw=2)

def init():
    for subject, subject_responses in subjects.items():
        all_subject_responses = []
        for response in subject_responses['responses']:
            all_subject_responses += response

        plt.hist(response, bins=bins, label=subject)
    
    cursor.set_data([0, 0], [0, 1])
    return (cursor,)

scale = 10
def animate(i):
    x = [i * scale, i * scale]
    y = [0, 1]
    cursor.set_data(x, y)
    return (cursor,)


# In[22]:

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=length//scale, interval=10, blit=True)
HTML(anim.to_html5_video())


# In[ ]:



