from pathlib import Path
import glob


path = Path('/Users/mamason6/Documents/workshops/hackweek-2024/data/A19 SnowPits')
flist = [] #unique
s_flist = []
n_flist = []

for i, file in enumerate(path.glob('*')):

    pitID = file.name.split('_')[5]
    pitID = pitID.split('.')[0]

    #unique flist
    flist.append(pitID)

flist = set(flist)


# for pitID in flist:
#     # print(pit)
#
#     if 'C' in pitID:
#         print('Cross line pits')
#         print(pitID)
#
#     elif 'N' in pitID:
#         print('North line pits')
#         print(pitID)
#
#     elif 'S' in pitID:
#         print('South line pits')
#         print(pitID)

# Initialize a dictionary to store the groups
groups = {'C': [], 'N': [], 'S': []}

# Loop through the list and group the items
for pit in flist:
    if 'C' in item:
        groups['C'].append(pit)
    if 'N' in item:
        groups['N'].append(pit)
    if 'S' in item:
        groups['S'].append(pit)

# Print the groups
print(groups)


# pit_list = ['1S1', '1S2', '2S3', '2S4', '3S5', '2S7', '2S6', '1S8']
#
# for item in pit_list:
#
# for file in path:
