from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import os 

## CREATING DATA DIRS
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
    ## PROCESSING TABLE
    data = pd.read_csv(file, header=None)
    data = data.apply(pd.to_numeric, errors='coerce')
    data.drop(0,axis=1,inplace=True)
    data.rename(columns={1:'raw_data',2:'processed_data'},inplace=True)

    ## EXTRACTING DATA
    name = file.split('\\')[-1].split('.')[0]
    freq = data['raw_data'][150:550]
    idx = data.index[150:550]

    ## STATISTICAL ANALYSIS
    array = np.array(freq)
    mean = array.mean()
    std = array.std()

    ## PLOTTING LINECHARTS
    plt.figure(figsize=(15,5))
    plt.plot(idx, freq)
    plt.title(f'name: {name}\nmean: {mean}\nstd: {std}', loc='center')
    #### SAVE PLOT
    plt.savefig(f'activity3\\lineCharts\\{name}.png')

    ## PLOTTING histograms
    plt.figure(figsize=(15,5))
    plt.hist(freq, bins=100)
    plt.title(f'name: {name}\nmean: {mean}\nstd: {std}', loc='center')
    #### SAVE PLOT
    plt.savefig(f'activity3\\histograms\\{name}.png')

    ## PLOTTING SIDE BY SIDE
    figure, axs = plt.subplots(nrows=1, ncols= 2, figsize=(20,7))
    #### LINECHART
    axs[0].plot(idx,freq)
    #### HISTOGRAM
    axs[1].hist(freq)
    #### SAVE PLOT
    figure.suptitle(f'name: {name}\nmean: {mean}\nstd: {std}')
    figure.savefig(f'activity3\\twoPlots\\{name}.png')

    ## PLOTTTING ZSCORE FREQ
    z_scoreFreq = [(f-mean)/std for f in freq]
    plt.figure(figsize=(15,5))
    plt.hist(z_scoreFreq, bins=100)
    plt.title(f'name: Z-Score {name}\nmean: {mean}\nstd: {std}', loc='center')
    #### SAVE PLOT
    plt.savefig(f'activity3\\z-scoreHistograms\\{name}.png')

print(z_scoreFreq)