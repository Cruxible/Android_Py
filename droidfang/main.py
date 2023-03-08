import getpass
import os
import socket
import time
import os
import sys
import shutil
import random
import datetime
#Treeview of dirctory_____________________________
from rich.tree import Tree
from rich import print

from roku import *
from def_droidfang import *

def main():
    os.system('clear')
    user = getpass.getuser()
    logo()
    oslogger()
    maindir = "/sdcard/bin/droidfang"
    os.chdir(maindir)
    while True:
        curdir = os.getcwd()
        print("_____________________________________" + "\n __ " + curdir )
        command = input("(____" + user + "_____: ")
        match command:
            case 'exit':
                os.system('clear')
                exit()
            case 'clear':
                os.system('clear')
                logo()
            case 'yt music':
                os.system('python3 audiodl.py')
            case 'yt video':
                os.system('python3 videodl.py')
            case 'roku on':
                rokuon()
                os.system('clear')
                logo()
            case 'roku home':
                rokuhome()
                os.system('clear')
                logo()
            case 'roku off':
                rokuoff()
                os.system('clear')
                logo()
            case 'volume up':
                volumeup()
                os.system('clear')
                logo()
            case 'volume down':
                volumedown()
                os.system('clear')
                logo()
            case 'roku select':
                rokuselect()
                os.system('clear')
                logo()
            case 'roku play':
                rokuplay()
                os.system('clear')
                logo()
            case 'roku back':
                rokuback()
                os.system('clear')
                logo()
            case 'roku up':
                rokuup()
                os.system('clear')
                logo()
            case 'roku down':
                rokudown()
                os.system('clear')
                logo()
            case 'roku left':
                rokuleft()
                os.system('clear')
                logo()
            case 'roku right':
                rokuright()
                os.system('clear')
                logo()
            case 'roku yt':
                youtuberoku()
                os.system('clear')
                logo()
            case 'list dir':
                os.system('clear')
                listdir()
                continue
            case 'cd database':
                os.system('clear')
                os.chdir('/sdcard/bin/droidfang/database')




if __name__ == "__main__":
    main()
