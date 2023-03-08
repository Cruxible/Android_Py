import os
import getpass
import time
import os
import sys
import pyfiglet
import datetime
import winsound
from rich.tree import Tree
from rich import print
from def_fang import logo
from def_fang import mainlogo
#ogre
#sblood
#doom
#drpepper
#epic
os.system('cls')
logo()
mainlogo()
print("___________________________________\n<-----------> fig <----------->\n___________________________________\n exit - to exit figlet")
user = getpass.getuser()
while True:
	curdir = os.getcwd()
	print("___________________________________" + "\n __ " + curdir )
	data = input("(--->" + user + "<--->: ")
	if data == 'exit':
		os.system('cls')
		logo()
		mainlogo()
		break
	else:
		result = pyfiglet.figlet_format(data,font='epic')
		os.system('clear')
		logo()
		print("___________________________________\n<-----------> fig <----------->\n___________________________________\n")
		print(result)
		print("___________________________________")
		break
		os.system('cls')
		logo()
		mainlogo()