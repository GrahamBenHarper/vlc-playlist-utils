# VLC-playlist-utils

Python-based utilities for creating VLC playlists by sorting files in a directory by metadata such as track number. This depends on the eyed3 package to read track metadata, which may be installed with
```
pip install eyed3
```
which is also noted in the requirements.txt file.

### Usage
To run this, use
```
python main.py -d DIRECTORY -s1 FIRST_SORT -s2 SECOND_SORT -s3 THIRD_SORT -s4 FOURTH_SORT
```
where `DIRECTORY` is the directory to start from, and the remaining three arguments are the sorting order chosen from the list `["artist","album","tracknum","discnum","title","filename",""]`. The default sort order is "artist","album","discnum","tracknum".