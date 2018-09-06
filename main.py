#****************************************************************

#uploads multiple files to Dropbox using Dropbox SDK and API
#input is canonical paths to files/directories that
#need to get uploaded

#****************************************************************

#from dropbox.exceptions import AuthError
from shutil import copyfile
from subprocess import call
import os
import re
import sys

#TOKEN = ' '
#directory where files will uploaded to Dropbox
dirname = '/home/Documents/'    

#local files that are to be uploaded
#take input from user
localfiles = input('Enter the canonical paths to files/directories you want to upload(like'
                ' /home/username/file), seperated by commas:\n').split(',')

no_of_dirs = 0
localfiles = [files.replace('~', os.environ['HOME']) for files in localfiles]

for files in localfiles:
    #if files is actually a directory, invoke shell script zipit.sh
    #there will be only one zip archive, directories will be added
    if os.path.exists(files):   #checking if the path exists
        if os.path.isdir(files):    #if exists, check if it's a file or a dir
            no_of_dirs += 1
            call(['./zipit.sh', re.sub(r'[\s+]', r'\ ', files)]) # in case path contains whitespaces

#create an instance of a Dropbox class, which can make requests to the API.
#dbox_obj = dropbox.Dropbox(fiload. timeout=None)

'''
#check for an access token
if (len(TOKEN) == 0):
    sys.exit("ERROR: Looks like you didn't add your access token. "
        "Kindly put your token in line 17 of the source code.")

#check that the access token is valid
try:
    dbox_obj.users_get_current_account()
except AuthError as err:
    sys.exit("ERROR: Invalid access token; try re-generating an access token")
'''

#upload.backup(dbox_obj)
#print("Uploading done!")


#*************************************************************
'''
#user-defined function for extracting file extension, if there is any
def get_exton(path_to_local_file):
    file_base = os.path.basename(path_to_local_file)
    start = len(file_base) - 1
    while start:
        if file_base[start] == '.':
            exton = file_base[start:len(file_base)-1]
            break
        start = start - 1
    return exton
'''
#**************************************************************
