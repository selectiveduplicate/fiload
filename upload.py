from dropbox.files import WriteMode
from dropbox.exceptions import ApiError
import main
import os
import sys 

#uploads contents of localfiles to Dropbox
def backup(api_obj):
    if main.no_of_dirs > 0: #if there is a directory
        with open('zipped.zip', 'rb') as f:
            print("Uploading the directory/ies in a single zip archive as " 
                    + main.dirname + "zipped.zip" + "...")
            try:
                api_obj.files_upload(f.read(), main.dirname + 'zipped.zip', 
                mode=WriteMode('overwrite'))
            except ApiError as err:
                #check if user has enough Dropbox space quota for uploading
                if (err.error.is_path() and
                    err.error.get_path().reason.is_insufficient_space()):
                    sys.exit("ERROR: Cannot upload; insufficient space.")
                elif err.user_message_text:
                    print(err.user_message_text)
                    sys.exit()
                else:
                    print(err)
                    sys.exit()
    if os.path.exists(os.getcwd()+'/zipped.zip'):
        os.remove(os.getcwd()+'/zipped.zip')

    for files in main.localfiles:
        #if directory, skip, because we've already done it above
        if os.path.isdir(files):
            continue
        backupAs = main.dirname + os.path.basename(files)
        with open(files, 'rb') as f:
            #using WriteMode=overwrite to make sure that the contents in the file
            #are changed on upload
            print("Uploading " + files + " to Dropbox as " + backupAs + "...")
            try:
                api_obj.files_upload(f.read(), backupAs , mode=WriteMode('overwrite'))
            except ApiError as err:
                #check if user has enough Dropbox space quota for uploading
                if (err.error.is_path() and
                    err.error.get_path().reason.is_insufficient_space()):
                    sys.exit("ERROR: Cannot back up; insufficient space.")
                elif err.user_message_text:
                    print(err.user_message_text)
                    sys.exit()
                else:
                    print(err)
                    sys.exit()
