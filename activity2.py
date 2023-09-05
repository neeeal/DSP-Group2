import os
import pandas as pd
from matplotlib import pyplot as plt

# for f in os.listdir():
#     if os.path.isdir('./'+f):
#         path = os.path.join('./'+f,
#         os.listdir()

root = "./activity2"
dirs = [dir for dir in os.listdir(root) if "."  not in dir]
files = []

for dir in dirs:
    # print(dir)
    nest_dir = os.path.join(root, dir)
    for f in os.listdir(nest_dir):
        filepath = os.path.join(nest_dir, f)
        files.append(filepath)
        
for file in files:
    data = pd.read_csv(file, header=None)
    data.drop(0,axis=1,inplace=True)
    data.rename(columns={1:'raw_data',2:'processed_data'},inplace=True)

    plt.figure(figsize=(15,5))
    plt.plot(data.index[200:500], data['raw_data'][200:500])
    name = file.split('\\')[-1].split('.')[0]
    print(name)
    plt.title(f'voice ({name})')
    plt.xlabel('time(ms)')
    plt.ylabel(data.columns[0])
    plt.show()