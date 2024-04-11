import os, sys

### OPTIONS

args = "-q:a 0 -map 0 -map_metadata 0"
output_folder_name = "change-container-output"

# if file was a specified argument
if (len(sys.argv) > 1):
    file_path = sys.argv[1]
# file needs to be specified.
else:
    file_path = input("please drag the specified file into the cmd window.\n")
    # remove quotes
    if (file_path[0] == "\"" or file_path[0] == "\'"):
        file_path = file_path[1:len(file_path)-1]

# if output format was a specified argument
if (len(sys.argv) > 2):
    new_container = sys.argv[2]
# output format needs to be specified.
else:
    new_container = input("what is the new file type wanted? (\".mp3\"/\".wav\", etc.)\n")
    
# if overwriting extension was specified
if (len(sys.argv) > 3):
    overwrite = sys.argv[3]
else:
    overwrite = input("overwrite old extension? (y/n) ")



### CONVERSION

# create output folder if it does not exist

if (not os.path.exists(sys.path[0] + "\\" + output_folder_name)):
    os.mkdir(sys.path[0] + "\\" + output_folder_name)

## setup modified_file

# isolate file_name
modified_file_path = file_path
modified_file_path = modified_file_path[len(modified_file_path) - file_path[::-1].index("\\"):]

if (overwrite == "y"):
    # remove old extension
    modified_file_path = modified_file_path[0:len(modified_file_path) - modified_file_path[::-1].index(".") - 1]

# add new extension
modified_file_path += new_container



## run the command
command = "ffmpeg -i "
command += "\"" + file_path + "\" " # add original file to command
command += args + " " # add FFMPEG arguments
command += "\"" + sys.path[0] + "\\change-container-output\\" + modified_file_path + "\"" # add output path

os.system(command)

if (len(sys.argv) < 3):
    os.system('pause')