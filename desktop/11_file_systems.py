import os

# # getcwd(): get current working directory
# print(os.getcwd())
# os.chdir("automation")
# print(os.getcwd())
# os.chdir("../..")
# print(os.getcwd())

# # file path
# file_path = os.path.join(os.getcwd(), "my_file.txt")
# print(file_path)

# # get folder info from file path
# folder_path = os.path.dirname(r"D:\CS\automation")

# # get file info
# import time
# import datetime

# # getctime(): file created time
# ctime = os.path.getctime("example.xlsx")
# print(ctime)
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# # getmtime(): file modified time
# # getatime(): file accessed time

# # getsize(): file size
# size = os.path.getsize(file_path)
# print(size)

# # listdir(NAME): get folder list under folder NAME (if given)
# print(os.listdir())
# print(os.listdir("automation"))

# # get file list
# result = os.walk("automation")
# for root, dirs, files in result:
#     print(root, dirs, files)

# searching files
name = "11_file_systems.py"
result = []
# for root, dirs, files in os.walk(os.getcwd()):
for root, dirs, files in os.walk("."):
    if name in files:
        result.append(os.path.join(root, name))

print(result)

# find files with pattern
import fnmatch

pattern = "*.py"
result = []
for root, dirs, files in os.walk("."):
    for name in files:
        if fnmatch.fnmatch(name, pattern):
            result.append(os.path.join(root, name))
print(result)
