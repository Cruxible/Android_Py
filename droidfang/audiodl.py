import getpass
import time
import os
import pytube
import shutil
from pytube import YouTube

from rich.tree import Tree
from rich import print

from def_droidfang import logo

os.system('clear')
logo()
user = getpass.getuser()
while True:
	maindir = "/sdcard/bin/droidfang/fangsongs"
	os.chdir(maindir)
	print("___________________________________")
	print("Youtube audio download")
	print("Please enter a url")
	print("type exit to exit download option")
	print("___________________________________" + "\n __ " + maindir)
	# url input from user
	x = (input("(--->" + user + "<--->: "))
	if x == "exit":
	    os.system('clear')
	    logo()
	    break
	else:
		yt = YouTube(x)  
		# extract only audio
		video = yt.streams.filter(only_audio=True).first()
		os.system('clear')
		logo() 
		# check for destination to save file
		print("Enter the destination (leave blank for current directory)")
		print("___________________________________" + "\n __ " + maindir)
		destination = str(input("(--->" + user + "<--->: ")) or '.'
		if destination == 'exit':
		 os.system('clear')
		 break 
		# download the file
		out_file = video.download(output_path=destination) 
		# save the file
		base, ext = os.path.splitext(out_file)
		new_file = base + '.mp3'
		os.rename(out_file, new_file)
		os.system('clear')
		logo()  
		# result of success
		print(yt.title + " has been successfully downloaded.")
		break
