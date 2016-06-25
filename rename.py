import os

def rename_files():
    # 1) ge file names from a folder
    #  2) for each file, rename filename
    file_list = os.listdir(r"/Users/albert/downloads/prank2")
    # print (file_list)
    saved_path = os.getcwd()
    # print ("current working dir is " + saved_path)
    os.chdir(r"/Users/albert/downloads/prank2")
    # #print os.getcwd()
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"0123456789"))
    os.chdir(saved_path)
    # print file_list
rename_files()
