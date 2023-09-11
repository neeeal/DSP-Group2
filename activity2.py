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

## INDIVIDUAL PLOTS
## HISTOGRAM
fig, axs = plt.subplots(3, 3)
axs[0, 0].hist(freqs[0])
axs[0, 0].set_title(names[0])
axs[1, 0].hist(freqs[1])
axs[1, 0].set_title(names[1])
axs[2, 0].hist(freqs[2])
axs[2, 0].set_title(names[2])
axs[0, 1].hist(freqs[3])
axs[0, 1].set_title(names[3])
axs[1, 1].hist(freqs[4])
axs[1, 1].set_title(names[4])
axs[2, 1].hist(freqs[5])
axs[2, 1].set_title(names[5])
axs[0, 2].hist(freqs[6])
axs[0, 2].set_title(names[6])
axs[1, 2].hist(freqs[7])
axs[1, 2].set_title(names[7])
axs[2, 2].hist(freqs[8])
axs[2, 2].set_title(names[8])
fig.tight_layout()
plt.show()

## LINE CHART
fig, axs = plt.subplots(3, 3)
axs[0, 0].plot(idxs[0],freqs[0])
axs[0, 0].set_title(names[0])
axs[1, 0].plot(idxs[1],freqs[1])
axs[1, 0].set_title(names[1])
axs[2, 0].plot(idxs[2],freqs[2])
axs[2, 0].set_title(names[2])
axs[0, 1].plot(idxs[3],freqs[3])
axs[0, 1].set_title(names[3])
axs[1, 1].plot(idxs[4],freqs[4])
axs[1, 1].set_title(names[4])
axs[2, 1].plot(idxs[5],freqs[5])
axs[2, 1].set_title(names[5])
axs[0, 2].plot(idxs[6],freqs[6])
axs[0, 2].set_title(names[6])
axs[1, 2].plot(idxs[7],freqs[7])
axs[1, 2].set_title(names[7])
axs[2, 2].plot(idxs[8],freqs[8])
axs[2, 2].set_title(names[8])
fig.tight_layout()
plt.show()

## COMPARING PLOTS
## COMPARING HISTOGRAMS
fig = plt.figure()
gs = fig.add_gridspec(4, hspace=0)
axs = gs.subplots(sharex=False, sharey=False)
axs[0].hist(freqs[0], color="red", alpha=0.5, label=names[0])
axs[0].hist(freqs[3], color="blue", alpha=0.5, label=names[3])
axs[0].legend(loc='upper right')
axs[0].set_title('Comparing Histograms')
# axs[0].set_title(f'{names[0]} and {names[3]}', y=1.0, pad=-14)
axs[1].hist(freqs[1], color="red", alpha=0.5, label=names[1])
axs[1].hist(freqs[4], color="blue", alpha=0.5, label=names[4])
axs[1].legend(loc='upper right')
# axs[1].set_title(f'{names[1]} and {names[4]}', y=1.0, pad=-14)
axs[2].hist(freqs[2], color="red", alpha=0.5, label=names[2])
axs[2].hist(freqs[5], color="blue", alpha=0.5, label=names[5])
axs[2].legend(loc='upper right')
# axs[2].set_title(f'{names[2]} and {names[5]}', y=1.0, pad=-14)
axs[3].hist(freqs[7], color="red", alpha=0.5, label=names[7])
axs[3].hist(freqs[8], color="blue", alpha=0.5, label=names[8])
axs[3].legend(loc='upper right')
# axs[3].set_title(f'{names[7]} and {names[8]}', y=1.0, pad=-14)
plt.show()

## COMPARING LINE CHARTS
fig = plt.figure()
gs = fig.add_gridspec(4, hspace=0)
axs = gs.subplots(sharex=False, sharey=False)
axs[0].plot(idxs[0], freqs[0], color="red", alpha=0.5 , label=names[0])
axs[0].plot(idxs[3], freqs[3], color="blue", alpha=0.5, label=names[3])
axs[0].legend(loc='upper right')
axs[0].set_title('Comparing Line Charts')
# axs[0].set_title(f'{names[0]} and {names[3]}', y=1.0, pad=-14)
axs[1].plot(idxs[1], freqs[1], color="red", alpha=0.5, label=names[1])
axs[1].plot(idxs[4], freqs[4], color="blue", alpha=0.5, label=names[4])
axs[1].legend(loc='upper right')
# axs[1].set_title(f'{names[1]} and {names[4]}', y=1.0, pad=-14)
axs[2].plot(idxs[2], freqs[2], color="red", alpha=0.5, label=names[2])
axs[2].plot(idxs[5], freqs[5], color="blue", alpha=0.5, label=names[5])
axs[2].legend(loc='upper right')
# axs[2].set_title(f'{names[2]} and {names[5]}', y=1.0, pad=-14)
axs[3].plot(idxs[7], freqs[7], color="red", alpha=0.5, label=names[7])
axs[3].plot(idxs[8], freqs[8], color="blue", alpha=0.5, label=names[8])
axs[3].legend(loc='upper right')
# axs[3].set_title(f'{names[7]} and {names[8]}', y=1.0, pad=-14)
plt.show()