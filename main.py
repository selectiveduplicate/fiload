#****************************************************************

#uploads multiple files to Dropbox using Dropbox SDK and API
#input is canonical paths to files/directories that
#need to get uploaded

#****************************************************************

from subprocess import call
import os
import re

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
            call(["bash", "zipit.sh", re.sub(r'[\s+]', r'\ ', files)]) # in case path contains whitespaces
