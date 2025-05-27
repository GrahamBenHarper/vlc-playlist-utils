import eyed3
import os

# print out a VLC playlist format with all tracks in a subdirectory sorted by track number

# grab all files in the path
rootpath = "/home/user/Music/"
renamepath = "/storage/0123-4567/Music/"
albums = os.listdir(rootpath)

# grab all albums in directory
for album in albums:
  if album.endswith(".mp3"):
    continue
  path = rootpath + album
  files = os.listdir(path)

  # Setup some lists for tracking data
  is_song = [file.endswith(".mp3") for file in files]
  track_nums = [0 for file in files]
  filepaths = [path + "/" + file for file in files]

  # grab the tracknum from each track
  for i,file in enumerate(files):
    if is_song[i]:
      f = eyed3.load(filepaths[i])
      if f.tag.track_num[0] != None:
        track_nums[i] = int(f.tag.track_num[0])
      else:
        print(f"No track data available for {filepaths[i]}")

  # create a list of indices for walking through tracks in order
  inds = [i[0] for i in sorted(enumerate(track_nums), key=lambda x:x[1])]

  # print out the VLC playlist file
  print('<?xml version="1.0" encoding="UTF-8"?>')
  print('<playlist version="1" xmlns="http://xspf.org/ns/0/">')
  print(f'<title>{album}</title>')
  print('<trackList>')
  for i in inds:
    filepathplaylist = filepaths[i].replace(rootpath,renamepath)
    print(f"<track><location>file://{filepathplaylist}</location></track>")
  print('</trackList>')
  print('</playlist>')

#print(f.tag.artist)
#print(f.tag.album)
#print(f.tag.title)
#print(f"{f.tag.track_num[0]}/{f.tag.track_num[1]}")
