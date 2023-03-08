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
print("Encrypting Data")
# Play Windows exit sound.
winsound.PlaySound('SystemHand', winsound.SND_ALIAS)
os.system('cls')
print("___________________________________\n<-----------> Enc Data <----------->\n___________________________________")
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
key = Fernet.generate_key()
with open("thekey1.key", "wb") as thekey:
        thekey.write(key)
for file in files:
        with open(file, "rb") as thefile:
                contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
                thefile.write(contents_encrypted)
                print("Files Encrypted")
# Play Windows exit sound.
winsound.PlaySound('SystemHand', winsound.SND_ALIAS)
print("Data Encrypted")