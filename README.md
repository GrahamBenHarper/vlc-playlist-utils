# VLC-playlist-utils

Python-based utilities for creating VLC playlists by sorting files in a directory by metadata such as track number.
Given a directory, this script recurses over all subdirectories and places an `.xspf` file containing all tracks in that subdirectory sorted according to the sort arguments.
The playlist filename is either given a number or named after the containing subdirectory.
The main use case for this is automatically generating playlists for devices using the VLC app,
as the playlists are automatically detected by the app when it searches the relevant music subdirectories.



## Dependencies

This depends on the eyed3 package to read track metadata, which may be installed with
```
pip install eyed3
```
which is also noted in the requirements.txt file.



## Usage

To run this, use
```
python main.py -d DIRECTORY -s1 FIRST_SORT -s2 SECOND_SORT -s3 THIRD_SORT -s4 FOURTH_SORT
```
where `DIRECTORY` is the directory to start from, and the remaining three arguments are the sorting order chosen from the list `["artist","album","tracknum","discnum","title","filename",""]`. The default sort order is "artist","album","discnum","tracknum".
Additionally, a `-p` or `--playlistname` option may be specified, which changes how the playlist files are named. The options for playlistname are "number" and "directory".



## How VLC playlists work

VLC playlists are most commonly specified by a file in the `.xspf` format, which uses XML style to define several attributes, as shown below for Gorillaz album Demon Days.

```
<?xml version="1.0" encoding="UTF-8"?>
<playlist version="1" xmlns="http://xspf.org/ns/0/">
<title>Demon Days</title>
<trackList>
<track><location>Gorillaz - Intro.mp3</location></track>
<track><location>Gorillaz - Last Living Souls.mp3</location></track>
<track><location>Gorillaz - Kids with Guns.mp3</location></track>
<track><location>Gorillaz - O Green World.mp3</location></track>
<track><location>Gorillaz, Bootie Brown - Dirty Harry.mp3</location></track>
<track><location>Gorillaz - Feel Good Inc..mp3</location></track>
<track><location>Gorillaz - El Mañana.mp3</location></track>
<track><location>Gorillaz - Every Planet We Reach Is Dead.mp3</location></track>
<track><location>Gorillaz, MF DOOM - November Has Come.mp3</location></track>
<track><location>Gorillaz, Martina Topley-Bird, Roots Manuva - All Alone.mp3</location></track>
<track><location>Gorillaz - White Light.mp3</location></track>
<track><location>Gorillaz - DARE.mp3</location></track>
<track><location>Gorillaz - Fire Coming out of the Monkey's Head.mp3</location></track>
<track><location>Gorillaz - Don't Get Lost in Heaven.mp3</location></track>
<track><location>Gorillaz - Demon Days.mp3</location></track>
</trackList>
</playlist>
```

The first two lines and last line are generic wrapping template material that's needed in every playlist.
The following `title` element specifies the playlist title.
Next is the `tracklist` element, which contains each of the tracks in order.
These entries are paths to the audio files for the tracks, which are wrapped by `track` and `location` elements.
The path may be a relative path to the playlist location or an absolute path.
This is the same format of playlist created by this script.



### Known issues with VLC playlists
If a file or directory contains unusual characters in the name, it can cause VLC to skip the playlist or track.
It's unclear exactly what causes it, but it seems like some sorts of obscure unicode or non-unicode characters cause the problem.
