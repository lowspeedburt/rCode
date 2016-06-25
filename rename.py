import os


def rename_files():
    # 1) ge file names from a folder
    #  2) for each file, rename filename
    file_list = os.listdir(r"/Users/aburthinds/Downloads/prank2")
    # print (file_list)
    saved_path = os.getcwd()
    # print ("current working dir is " + saved_path)
    os.chdir(r"/Users/aburthinds/Downloads/prank2")
    print(os.getcwd())
    for file_name in file_list:
        s = str.maketrans("", "", "0123456789")
        os.rename(file_name, file_name.translate(s))
    os.chdir(saved_path)
    print(file_list)
    print(os.getcwd())

    # s = "abcdef"
    # r = s.replace("a", "H")
    # print (r)


rename_files()











# def by_three(number):
#     divBy = ((number % 3) == 0)
#     if (divBy):
#         print("this is okay")
#     else:
#         print("nope")

# by_three(3)

#
# array = [2,6,1,107,15,66]
#
# def biggestNum(args):
#     print(max(args))
#     return max(args)
#
#
# biggestNum(array)
