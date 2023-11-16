import os
import shutil
ext=input()
source_folder='/home/navaneeth/amfoss_tasks'
dest_folder='/home/navaneeth/new'
for folderName, subfolders, filenames in os.walk('/home/navaneeth/amfoss_tasks'):
    for filename in filenames:
        if filename.endswith('.'+ext):
            source_path=os.path.join(folderName,filename)
            dest_path=os.path.join(dest_folder,filename)
            shutil.copy(source_path,dest_path)
        else:
            continue