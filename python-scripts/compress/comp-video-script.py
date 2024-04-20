import subprocess
import os
import sys


output_folder_name = "compressed"

## get essential data to convert

# if file was a specified argument
if (len(sys.argv) > 1):
    file_path = sys.argv[1]
# file needs to be specified.
else:
    file_path = input("please drag the specified file into the cmd window.\n")
    # remove quotes
    if (file_path[0] == "\"" or file_path[0] == "\'"):
        file_path = file_path[1:len(file_path)-1]

print("\ntarget can be inaccurate, may require a lower number than it seems it should")
target = input("target bitrate? (in mb, ex. \'25\'): ")



file_name = file_path[-(file_path[::-1].index('\\')):]
file_name = file_name[:len(file_name) - file_name[::-1].index('.') - 1]
parent_dir = os.getcwd()
duration = subprocess.getoutput("MediaInfo --Output=Video;%Duration% " + "\"" + file_path + "\"")
total_rate = ((int)(target) * 8192) / (int(float(duration)) / 1000)
audio_track_count = subprocess.getoutput("MediaInfo --Output=General;%AudioCount% " + "\"" + file_path + "\"")
enabled_tracks = []

# create directory if it doesn't exist
if not os.path.exists(parent_dir + "\\" + output_folder_name):
    os.makedirs(parent_dir + "\\" + output_folder_name)
    
# see what tracks are enabled
for x in range(int(audio_track_count)):
    if (input("keep audio track " + str(x+1) + "? (y/n) ") == "y"):
        enabled_tracks.append(True)
    else:
        enabled_tracks.append(False)
# generate part of command for keeping and removing tracks
track_data = "-filter_complex \""
enabled_count = 0
all_disabled_query = True
for x, value in enumerate(enabled_tracks):
    if value:
        all_disabled_query = False
        track_data = track_data + "[0:a:" + str(x) + "]"
        enabled_count += 1
if (all_disabled_query):
    track_data = "-an"
else:
    track_data += "amerge=inputs=" + str(enabled_count) + "\""

# run ffmpeg commands and rename output 
# not sure why but I used to have this option included : -vf scale=1920:1080
print("ffmpeg -i \"" + file_path + "\" -b:v " + str(total_rate*.75) + "k -b:a " + str(total_rate*.25) + "k " + track_data + "\"" + " \"" + parent_dir + "\\Compressed\\" + file_name + "-compressed--mb.mp4")
os.system("ffmpeg -i \"" + file_path + "\" -b:v " + str(total_rate*.75) + "k -b:a " + str(total_rate*.25) + "k " + track_data + " \"" + parent_dir + "\\Compressed\\" + file_name + "-compressed--mb.mp4")
file_size = subprocess.getoutput("MediaInfo --Output=General;%FileSize/String% " + "\"" + parent_dir + "\\Compressed\\" + file_name + "-compressed--mb.mp4\"")
file_size = file_size[0:4]
os.system("rename " + "\"" + parent_dir + "\\Compressed\\" + file_name + "-compressed--mb.mp4\" \"" + file_name + "-compressed" + file_size + "mb.mp4\"")
os.system('')
os.system('pause')