from pathlib import Path
import shutil

path_in = Path('/Users/mamason6/Documents/workshops/hackweek-2024/data/A19 SnowPits')

# make path_in/photos directory
photos_dir = path_in / 'photos'
photos_dir.mkdir(exist_ok=True)

# make path_in/parameter_files directory
param_files_dir = path_in / 'parameter_files'
param_files_dir.mkdir(exist_ok=True)

# make path_in/photos/book directory
book_dir = photos_dir / 'book'
book_dir.mkdir(parents=True, exist_ok=True)

for i, file in enumerate(path_in.glob('*')):
    date = file.name.split('_')[4] # format = yyyymmdd

    # 1. parse all .jpg files into path_in/photos/yyyymmdd/ by unique date
    if file.suffix.lower() == '.jpg':
        if '_book' in file.name:
            # move .jpg files containing _book to the book directory
            shutil.move(str(file), str(book_dir / file.name))
        else:
            # move other .jpg files into date-based subdirectories
            date_dir = photos_dir / date
            date_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(file), str(date_dir / file.name))

    # 2. parse all .csv or .xlsx into path_in/parameter_files/yyyymmdd by unique date
    elif file.suffix.lower() in ['.csv', '.xlsx']:
        date_dir = param_files_dir / date
        date_dir.mkdir(parents=True, exist_ok=True)
        shutil.move(str(file), str(date_dir / file.name))









# from pathlib import Path
# import datetime
# import glob
# import shutil
#
# path_in = Path('/Users/mamason6/Documents/workshops/hackweek-2024/data/A19 SnowPits')
#
# # make path_in/photos directory
# photos_dir = path_in / 'photos'
# photos_dir.mkdir(exist_ok=True)
#
# # make path_in/parameter_files directory
# param_files_dir = path_in / 'parameter_files'
# param_files_dir.mkdir(exist_ok=True)
#
# for i, file in enumerate(sorted(path_in.glob('*'))):
#     print(i, file.name)
#     date = file.name.split('_')[4] # format = yyyymmdd
#
#     # 1. parse all .jpg files into path_in/photos/yyyymmdd/ by unique date
#     if file.suffix.lower() == '.jpg':
#         date_dir = photos_dir / date
#         date_dir.mkdir(parents=True, exist_ok=True)
#         shutil.move(str(file), str(date_dir / file.name))
#
#     # 2. parse all .csv or .xlsx into path_in/parameter_files/yyyymmdd by unique date
#     elif file.suffix.lower() in ['.csv', '.xlsx']:
#         date_dir = param_files_dir / date
#         date_dir.mkdir(parents=True, exist_ok=True)
#         shutil.move(str(file), str(date_dir / file.name))
