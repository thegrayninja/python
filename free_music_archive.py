#steps:
#set download page to 10000 (or whatever)
#http://freemusicarchive.org/genre/Hip-Hop/?sort=track_date_published&d=1&page=1&per_page=10000
#save contents to file
#curl -o full_page.txt <link>
#grep file
#grep "https://freemusicarchive.org/music/download" full_page.txt >> music_listings.txt
#open file and remove everything but the filename, then save
#change music_file = music_listings.txt
#after script is done, import audio into your music player and enjoy :)


import os			#allows for the wget command to run

music_file = "hip_hop_test.txt"

with open (music_file, "r") as music_data_file:
	for i in music_data_file:
		#print(i.strip())
		i2 = i.strip()
		formatwget = 'wget https://freemusicarchive.org/music/download/%s' % (i2)
		rename_file = 'mv %s %s.mp3' % (i2, i2)
		os.system(formatwget)
		os.system(rename_file)
