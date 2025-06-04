import eyed3
import os
import argparse

# starting from a root directory, walk through all nested subdirectories, and create a VLC playlist file
# for each subdirectory with all tracks in just the subdirectory.
# the playlist is sorted first by album name and then track number

renamepath = ""

def create_playlist(dir_name : str, outfile : str):
  """
  Finds all mp3 files in a full path given by dir_name.
  Then collects the tracknums for each mp3 from the metadata if it is present.
  Then writes out a playlist file to outfile in exactly the format vlc expects.
  Format documentation located at https://wiki.videolan.org/XSPF/
  """
  # find all mp3s in the current directory, initialize data to 0 or empty
  tracks = [f.name for f in os.scandir(dir_name) if os.path.isfile(f) and f.name.endswith(".mp3")]
  if tracks == []:
    return
  track_nums = [0 for track in tracks]
  filepaths = [dir_name + "/" + track for track in tracks]
  album_data = ["" for track in tracks]
  artist_data = ["" for track in tracks]
  title_data = ["" for track in tracks]
  
  #print(tracks)
  #print(filepaths)

  # view the metadata with eyed3 and load all track numbers into track_nums
  for i,track in enumerate(tracks):
    f = eyed3.load(filepaths[i])
    if f.tag.track_num[0] != None:
      track_nums[i] = int(f.tag.track_num[0])
    else:
      print(f'No track data available for {filepaths[i]}')
    if f.tag.artist != None:
      artist_data[i] = str(f.tag.artist)
    if f.tag.album != None:
      album_data[i] = str(f.tag.album)
    if f.tag.title != None:
      title_data[i] = str(f.tag.title) 

  # create a list of indices for walking through tracks in order
  # the order is specified hierarchically by the zip(album_data,track_nums)
  # meaning it will compare album names first, then compare track numbers
  inds = [i[0] for i in sorted(enumerate(zip(album_data,track_nums)), key=lambda x:x[1])]

  # alternatively, sort by filenames
  # inds = [i[0] for i in sorted(enumerate(filepaths), key=lambda x:x[1])]

  # print out the VLC playlist file, nameded with the directory
  playlist_name = dir_name.split("/")[-1]

  # name the file based on the outfile parameter
  f = open(dir_name + "/" + outfile,'w')

  # alternatively, create a filename based on the directory
  #f = open(dir_name + "/" + playlist_name.replace(" ","_") + ".xspf",'w')

  f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
  f.write('<playlist version="1" xmlns="http://xspf.org/ns/0/">\n')
  f.write(f'<title>{playlist_name}</title>\n') # TODO: cleanup use of global vars
  f.write('<trackList>\n')
  for i in inds:
    filepathplaylist = filepaths[i].replace(rootpath,renamepath).split("/")[-1] # TODO: cleanup use of global vars
    f.write(f'<track><location>{filepathplaylist}</location></track>\n')
  f.write('</trackList>\n')
  f.write('</playlist>\n')
  f.close()


parser = argparse.ArgumentParser(prog='create-vlc-playlists',
                                 description='Create playlists in the specified directory and subdirectories by sorting the tracks according to the sort parameters')
parser.add_argument("-d", "--directory", default="/home/user/Music", help="The directory where the playlists are created")
vars = parser.parse_args()

rootpath = vars.directory

# walk over all subdirectories of rootpath and create a playlist for each one
dirs = [d[0] for d in os.walk(rootpath)]
for i,dir_name in enumerate(dirs):
  print(i,dir_name)
  playlistfiles = [f.name for f in os.scandir(dir_name) if os.path.isfile(f) and f.name.endswith(".xspf")]
  if playlistfiles == []:
    create_playlist(dir_name, str(i) + ".xspf")
