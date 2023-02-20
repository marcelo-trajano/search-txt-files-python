import os

root_dir = "C:\\Users\\marce\\Desktop" # Change this to the root directory you want to search in
txt_files = []

for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".txt"):
             txt_files.append(os.path.join(subdir, file))


for file in txt_files:
    print(file)