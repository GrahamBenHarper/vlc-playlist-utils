# VLC-playlist-utils

Python-based utilities for creating VLC playlists by sorting files in a directory by metadata such as track number. This depends on the eyed3 package to read track metadata, which may be installed with
```
pip install eyed3
```
which is also noted in the requirements.txt file.

This supports a few different sorting algorithms, but currently requires modifying source to change them. An argument parser will include these capabilities.
