import os, sys

output_folder_name = "change-container-output"
# create output folder if it does not exist

if (not os.path.exists(sys.path[0] + "\\" + output_folder_name)):
    os.mkdir(sys.path[0] + "\\" + output_folder_name)
    

files = os.listdir(sys.path[0])
files.remove("change-container.py")
files.remove("change-containers.py")
files.remove(output_folder_name)

for x, file in enumerate(files):
    print(str(x + 1) + "     " + file)
    fileCount = x + 1
if (input("convert these " + str(fileCount) + " files? (y/n) ") == "n"):
    os.system('pause')
    
new_container = input("what is the new file type wanted? (\".mp3\"/\".wav\", etc.)\n")
overwrite = input("overwrite old extension? (y/n)\n")
for file in files:
    os.system("change-container.py \"" + sys.path[0] + "\\" + file + "\"" + " " + new_container + " " + overwrite)
os.system('pause')
