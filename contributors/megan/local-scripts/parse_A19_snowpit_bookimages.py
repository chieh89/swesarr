from pathlib import Path
import shutil

path_in = Path('/Users/mamason6/Documents/workshops/hackweek-2024/data/A19 SnowPits/photos')

# make path_in/photos/book directory
book_dir = path_in / 'book'
book_dir.mkdir(parents=True, exist_ok=True)

for i, file in enumerate(path_in.rglob('*')):
    if '_book' in file.name:
        shutil.move(str(file), str(book_dir / file.name))
