import os, sys, subprocess

# -- INSTRUCTIONS -- 
#
#   Put this script in a folder with media files containing comments.
#   Create a subfolder named "Overwritten" containing media files that 
#       share the first 27 letters of the media files in the main folder.
#   Run script and comments will be copied from main folder files to the
#       corresponding files in Overwritten.
#

# load in all files in script parent and grab their comments
print("processing source files...")
files = os.listdir(sys.path[0])
comments = []
files.remove("comment-tag-writer.py")
files.remove("Overwritten")
for x, file in enumerate(files):
    comments.append(subprocess.getoutput("MediaInfo --Output=General;%Comment% " + "\"" + file + "\""))
    print(str(x + 1) + "     " + file + "             " + comments[x])
print('confirm')
os.system('pause')
print()

# load in all the files where the comments will be transported
print("processing destination files...")
destFiles = os.listdir(sys.path[0] + "\\Overwritten\\")
for x, destFile in enumerate(destFiles):
    print(str(x + 1) + "     " + destFile)
print('confirm')
os.system('pause')
print()


# check to see if the destination file names are included in the original file names. Print all files missing corresponding files
print('starting')
missingFiles = []
for x, file in enumerate(files):
    found = False;
    for y, destFile in enumerate(destFiles):
        if (destFile[0:27] in file):
            os.system("atomicparsley \"Overwritten\\" + destFile + "\" --overWrite --comment \"" + comments[x] + "\"")
            found = True;
    if (not found):
        missingFiles.append(file)
        
print("\n")
print('missing counterparts to:')
for file in missingFiles:
    print(file)
    
print("\n")
os.system('pause')