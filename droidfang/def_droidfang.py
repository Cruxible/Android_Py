import os
import time
import datetime
from rich.tree import Tree
from rich import print
import pyfiglet

def listdir():
 maindir = ""
 os.chdir(maindir)
 x = os.listdir()
 curdir = os.getcwd()
 tree = Tree("[red1]" + curdir, guide_style="blue")
 for i in x:
        tree.add("[cyan1]" + str(i))
 print(tree)


def logo():
 x = ["\n @@@@@@@@  @@@@@@  @@@  @@@  @@@@@@@", " @@!      @@!  @@@ @@!@!@@@ !@@", " @!!!:!   @!@!@!@! @!@@!!@! !@! @!@!@", " !!:      !!:  !!! !!:  !!! :!!   !!:", "  :        :   : : ::    :   :: :: :"]
 for line in x:
     time.sleep(.2)
     print(line)
 print("_____________________________________")
 print("\n", time.asctime()) # print the GMT local time in readable format

def oslogger():
	maindir1 = "/sdcard/bin/droidfang/fangfiles"
	os.chdir(maindir1)
	f = open("logger.txt", "a")
	time_object = time.localtime() # local time
	time_object = time.gmtime()
	time.strftime(str(time_object))
	  # UTC time
	local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
	f.write("\nSession start time : " + local_time)
	f.close()

	# open file in read mode
	with open(r"logger.txt", 'r') as fp:
	    for count, line in enumerate(fp):
	        pass
	print(' OS Run Count:', count + 1)
	fp.close()

#ASCIIART_______________________________
def asciiart():
	os.system('clear')
	logo()
	print("___________________________________\n<-----------> fig <----------->\n___________________________________\n exit - to exit figlet")
	maindir = "/storage/emulated/0/bin/tpadroid/fangfiles"
	os.chdir(maindir)
	path = '/'
	user = getpass.getuser()
	while True:
		curdir = os.getcwd()
		print("___________________________________" + "\n __ " + curdir )
		data = input("(--->" + user + "<--->: ")
		if data == 'exit':
			os.system('clear')
			logo()
			clock()
			comlogo()
			break
		else:
			result = pyfiglet.figlet_format(data)
			os.system('clear')
			print("___________________________________\n<-----------> fig <----------->\n___________________________________\n")
			print(result)
			print("___________________________________")
			break
