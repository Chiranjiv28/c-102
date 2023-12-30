import os
import shutil

from_dir = "C:/Users/Chiranjiv/Downloads"
to_dir= "C:/Users/Chiranjiv/Desktop/DownloadedFiles"


list_of_files= os.listdir(from_dir)
for filename in list_of_files:
    name,extenstion= os.path.splitext(filename)

    if extenstion == "":
        continue 
    if extenstion in ['.png','.jpeg','.jpg','.webp','.gif','.jfif']:
        path1= from_dir + "/" + filename
        path2= to_dir + "/" + "imagefiles" 
        path3= to_dir + "/" + "imagefiles" + "/" + filename

        if os.path.exists(path2):
            print("moving files")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving files")
            shutil.move(path1,path3)

        
        
 
