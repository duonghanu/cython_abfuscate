import os
from config import ROOTDIR, EXCLUDE

for root, subdirs, files in os.walk(ROOTDIR):
    for file_name in files:
        #if '__pycache__' in subdirs:
        #    directory_to_remove = root+'/__pycache__'
        #    os.remove(directory_to_remove)
        #    print("directory "+directory_to_remove+" deleted")#to_debug
        if file_name[-4:]==".pyc":
            file_to_remove = root+'/'+file_name
            os.remove(file_to_remove)
            print("file "+file_to_remove+" deleted")
        if file_name[-3:]==".py" and file_name not in EXCLUDE:
            file_to_remove = root+'/'+file_name
            file_to_remove_c = root+'/'+file_name[:-2]+'c'
            os.remove(file_to_remove)
            os.remove(file_to_remove_c)
            print("file "+file_to_remove+" deleted")
            print("file "+file_to_remove_c+" deleted")