from subprocess import call 			#allows for the curl command to run


text_file = open("getWebServer_urls.txt", "r")	#opens local text file in read mode. 
						#text file is in columns, each site on
						#a new row

urlList = text_file.readlines()			#reads the text file, stores it as urlList
urlList = [i.replace('\n', '') for i in urlList]#removes returns, else curl gets an error

for x in urlList:				#task finally beings
	print(x)				#for ease of reading, testing
	call(['curl', '-I', x])			#performs the header pull via curl -I <site>


