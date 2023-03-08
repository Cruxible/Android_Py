import getpass
import time
import os
import sys
import winsound
from cryptography.fernet import Fernet
import shutil
import random
import datetime

from rich.tree import Tree
from rich import print

from def_fang import logo
from def_fang import mainlogo

os.system('cls')
logo()
mainlogo()
print("Decrypting Data")
# Play Windows exit sound.
winsound.PlaySound('SystemHand', winsound.SND_ALIAS)
os.system('cls')
print("___________________________________\n<-----------> Dec Data <----------->\n___________________________________")
files = []
data = "D:\\bin\\fang\\database"
os.chdir(data)
for file in os.listdir():
        if file == "thekey1.key":
                continue
        if os.path.isfile(file):
                files.append(file)
for file in os.listdir():
	print(file)
with open("thekey1.key", "rb") as key:
        secretkey = key.read()
secretphrase = "Dark"
user_phrase = input("Enter the secret phrase: ")
os.system('clear')
if user_phrase ==secretphrase:
		# Play Windows exit sound.
		winsound.PlaySound('SystemHand', winsound.SND_ALIAS)
		print("Data Decrypted")
		for file in files:
			with open(file, "rb") as thefile:
				contents = thefile.read()
			contents_decrypted = Fernet(secretkey).decrypt(contents)
			with open(file, "wb") as thefile:
				thefile.write(contents_decrypted)
				if(os.path.isfile("thekey1.key")):
					os.remove("thekey1.key")
					print("Files Decrypted")
					print("key Deleted successfully")
				else:
					print("File does not exist")
				#Showing the message instead of throwig an error
else:
        print("Access Denied")