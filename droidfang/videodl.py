import getpass
import time
import os
import pytube
import shutil
from pytube import YouTube

from rich.tree import Tree
from rich import print

from def_droidfang import *

os.system('clear')
logo()
user = getpass.getuser()
while True:
	maindir = "/sdcard/bin/droidfang/fangideos"
	os.chdir(maindir)
	print("___________________________________")
	print("Youtube Download")
	print("Please enter a url")
	print("type exit to exit download option")
	print("___________________________________" + "\n __ " + maindir)
	url = input("(--->" + user + "<--->: ")
	if url == 'exit':
		os.system('clear')
		logo()
		break
	#path = input("Enter A Path: ")
	pytube.YouTube(url).streams.get_highest_resolution().download(maindir)
	os.system('clear')
	logo()
	print('Youtube video successfully downloaded!')  
	break
