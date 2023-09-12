import os
import pandas as pd
from matplotlib import pyplot as plt

## Creating Dirs
root = "./activity2"
dirs = [dir for dir in os.listdir(root) if "."  not in dir]
files = []

for dir in dirs:
    nest_dir = os.path.join(root, dir)
    for f in os.listdir(nest_dir):
        filepath = os.path.join(nest_dir, f)
        files.append(filepath)

## SAVING DATA TO LISTS
freqs = []
names = []
idxs = []
for file in files:
    data = pd.read_csv(file, header=None)
    data.drop(0,axis=1,inplace=True)
    data.rename(columns={1:'raw_data',2:'processed_data'},inplace=True)
    names.append(file.split('\\')[-1].split('.')[0])
    freqs.append(data['raw_data'][200:500])
    idxs.append(data.index[200:500])

def plot_hists(rows, columns, data, title):
    fig, axs = plt.subplots(rows, columns)
    counter = 0
    for row in range(rows):
        for column in range(columns):
            axs[row, column].hist(data[counter])
            axs[row, column].set_title(title[counter])
            counter+=1
    fig.tight_layout()
    plt.show()

def plot_lines(rows, columns, index, data, title):
    fig, axs = plt.subplots(rows, columns)
    counter = 0
    for row in range(rows):
        for column in range(columns):
            axs[row, column].plot(index[counter], data[counter])
            axs[row, column].set_title(title[counter])
            counter+=1
    fig.tight_layout()
    plt.show()

def plot_compare(axis, ref_data, data, graph):
    if graph == 'hist':
        axs[axis].hist(freqs[ref_data], color="red", alpha=0.5, label=names[ref_data])
        axs[axis].hist(freqs[data], color="blue", alpha=0.5, label=names[data])
        axs[axis].legend(loc='upper right')
    if graph == 'line':
        axs[axis].plot(idxs[ref_data], freqs[ref_data], color="red", alpha=0.5, label=names[ref_data])
        axs[axis].plot(idxs[data], freqs[data], color="blue", alpha=0.5, label=names[data])
        axs[axis].legend(loc='upper right')

plot_hists(3, 3, freqs, names)
plot_lines(3, 3, idxs, freqs, names)

fig = plt.figure()
gs = fig.add_gridspec(4, hspace=0)
axs = gs.subplots(sharex=False, sharey=False)
plot_compare(0, 0, 3, 'hist')
plot_compare(1, 1, 4, 'hist')
plot_compare(2, 2, 5, 'hist')
plot_compare(3, 7, 8, 'hist')
plt.suptitle('Comparing Histograms')
plt.show()

fig = plt.figure()
gs = fig.add_gridspec(4, hspace=0)
axs = gs.subplots(sharex=False, sharey=False)
plot_compare(0, 0, 3, 'line')
plot_compare(1, 1, 4, 'line')
plot_compare(2, 2, 5, 'line')
plot_compare(3, 7, 8, 'line')
plt.suptitle('Comparing Line Charts')
plt.show()