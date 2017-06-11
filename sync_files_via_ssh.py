#github.com/thegrayninja
#python - backup files

##follow this guide to auth via key
##https://help.ubuntu.com/community/SSH/OpenSSH/Keys
##mkdir ~/.ssh			or cd..if it exists
##chmod 700 ~/.ssh    	not needed if it already exists
##ssh-keygen -t rsa
##ssh-copy-id <username>@<host>
##then, ssh once to <username>@<host> to enable auto-login


import os


originalFile = "/dir/path/tempfile.txt"
musicDir = "/dir/path/"
daysToSync = raw_input("Days to Sync: ")
os.system('find %s -mtime -%s -type d -print > %s' % (musicDir, daysToSync, originalFile))
os.system('sed -i -e "1d" %s' % (originalFile))



with open (originalFile, "r") as sync_dirs:
	for i in sync_dirs:
		clean_dir = i.strip()
		folder_name = clean_dir.replace("/dir/path", "")
		folder_name = folder_name.replace(" ","\\ ")
		print(clean_dir)
		print(folder_name)
		shouldSync = raw_input("Do you want to Sync this Directory? (y/n): ")
		if shouldSync == "y":
			print("directory will sync")
			os.system("scp -r '%s/' user@192.168.1.5:'/mnt/dir/path/Expansion\\ Drive/Music/%s/'" % (clean_dir, folder_name))
		else:
			print("skipped")

print("DONE!")
