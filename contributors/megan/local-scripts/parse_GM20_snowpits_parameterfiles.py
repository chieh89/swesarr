from pathlib import Path
import shutil

# ------------------------------------------------------------------------------
# Functions --------------------------------------------------------------------
# ------------------------------------------------------------------------------
def extract_pitData_swesarr_ROI(path_out, filepaths):

    path_photos = path_out / 'photos'
    path_photos.mkdir(exist_ok=True)

    path_parameters = path_out / 'parameter_files'
    path_parameters.mkdir(exist_ok=True)

    for file in filepaths:
        # print(file)
        # print(path_out / file.name)
        # print('\n')

        if file.suffix == '.jpg':
            print(file)
            print(path_photos / file.name)
            print('\n')
            shutil.copy(file, path_photos / file.name)
        else:
            print(file)
            print(path_parameters / file.name)
            print('\n')
            shutil.copy(file, path_parameters / file.name)

# ------------------------------------------------------------------------------
# Body --------------------------------------------------------------------
# ------------------------------------------------------------------------------

# paths
path_in = Path('/Users/mamason6/Documents/workshops/hackweek-2024/data/GM20 SnowPits')
path_out = Path('/Users/mamason6/Documents/workshops/hackweek-2024/data/GM20 SnowPits/swesarr-roi')
path_out.mkdir(exist_ok=True)

# static variables
# SWESARR ROI - list of snow pits in ROI
pits_roi = ["_1S1_", "_1S2_", "_1S8_", "_2S3_", "_2S4_", "_2S6_", "_2S7_", "_3S5_"]

# list of all files (searches recursively)
all_files = list(path_in.rglob('*'))


# filter file list for pits in SWESARR-ROI
filtered_files = [f for f in all_files if any(pit in f.stem for pit in pits_roi)]

# print(*filtered_files, sep='\n')

extract_pitData_swesarr_ROI(path_out, filtered_files)


# for i, file in enumerate(sorted(path_in.rglob('*'))):
#     # print(file.name)
#     if file.is_dir():
#         print(file)
#         # continue

    # extract_pitData_swesarr_ROI(path_out, file, pits_roi)
#
#
#
#
# # # make path_out/snow_temperature_profiles directory
# temp_files_dir = path_out / 'snow_temperature_profiles'
# temp_files_dir.mkdir(exist_ok=True)
#
# # SWESARR ROI - list of snow pits in ROI
# pits_roi = ["1S1", "1S2", "1S8", "2S3", "2S4", "2S6", "2S7", "3S5"]
#
#
# for i, file in enumerate(sorted(path_in.rglob('*_temperature_*'))):
#     # print('fname is: ', file.name)
#
#     # extract pitID from filename
#     pitID = file.name.split('_')[-3]
#
#     # select temperature profiles for pits in pit-ROI list
#     if pitID in pits_roi:
#         # print(file.name)
#
#         # copy temperature profiles of interest
#         shutil.copy(file, temp_files_dir / file.name)
#
#         # print(file)
#         # print(temp_files_dir / file.name)
#         # print('\n')
