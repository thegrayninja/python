# sudo apt install python3-pip
# sudo python3 -m pip install playsound

##
# things to fix:
# look for music specific files (ie: mp3, flac) --done
# ask for specific directory (...not useful for automated devices) --done, via config.py
# show artist and song title during playback, not full path
# once all songs have been played, restart random playback again --done

import os, random

from pathlib import Path
from playsound import playsound

try:
    import config
    musicDir = config.MusicDirectory
    NumberOfPlaythroughs = config.NumberOfPlaythroughs

except:
    print("import configy failed")
    homeDir = str(Path.home())
    musicDir = "{}/Music".format(homeDir)
    NumberOfPlaythroughs = 1


def main():
    print("""
We aren't smart here. We simply look at the default music
directory located in your home directory.

We then only look for three levels - Artist, Album, Song.

If no Albums exist, we'll take the songs from each artist. """)

    Playthroughs(NumberOfPlaythroughs)
    #PlayMusic()

    return 0


def Playthroughs(NumberOfPlaythroughs):
    ptcount = 1
    if NumberOfPlaythroughs == 0:
        while NumberOfPlaythroughs == 0:
            print("Playthrough Count: {}".format(ptcount))
            PlayMusic()
            ptcount += 1
    else:
        while NumberOfPlaythroughs > 0:
            print("Playthrough Count: {}".format(ptcount))
            PlayMusic()
            NumberOfPlaythroughs -= 1
            ptcount += 1
    return 0




def PlayMusic():
    TrackListing = GetTrackListing()

    NumberOfTracks = len(TrackListing)
    while NumberOfTracks > 0:
        print("Number of Tracks remaining: {}".format(NumberOfTracks))
        TrackNumber = random.randint(1,NumberOfTracks)
        SongToPlay = TrackListing.pop(TrackNumber-1)
        print(SongToPlay)
        playsound(SongToPlay)
        NumberOfTracks = len(TrackListing)

    #for Track in TrackListing:
        #print(Track)
    return 0


def GetTrackListing():
    SongLibrary = []
    MusicFileExt = [".mp3",".ogg","flac",".wav"]

    for Artist in os.listdir(musicDir):
        hasAlbum = 0
        print("\n{}".format(Artist))
        try:
            for Album in os.listdir("{}/{}/".format(musicDir,Artist)):
                try:
                    AlbumSongList = []
                    for Song in os.listdir("{}/{}/{}/".format(musicDir,Artist,Album)):
                        #print("\t{}".format(Song))
                        if Song[-4:] in MusicFileExt:
                            AlbumSongList.append(Song)
                            SongLibrary.append("{}/{}/{}/{}".format(musicDir,Artist,Album,Song))
                    print("\t{}".format(Album))
                    hasAlbum = 1
                    if AlbumSongList:
                        for i in AlbumSongList:
                            print("\t\t{}".format(i))
                    else:
                        print("\t\tNo Songs")

                except:
                    try:
                        SongList = []
                        Song = Album
                        if Song[-4:] in MusicFileExt:
                            SongList.append(Song)
                            SongLibrary.append("{}/{}/{}".format(musicDir,Artist,Song))
                        if SongList:
                            print("\t<<not part of an album>>")
                            for i in SongList:
                                print("\t\t{}".format(i))
                        else:
                            print("No Songs Found")

                    except:
                        continue
        except:
            print("Bad directory - there is no music here.")

    return SongLibrary


if __name__ == main():
    main()
