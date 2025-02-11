import os
# cwd =os.getcwd()
# print("this is current working dir", cwd)


# def get_dir():
#     print("current working dir before")
#     print(os.getcwd())
#     print()
# get_dir()
# os.chdir('../')
# get_dir()

file = open("p1.py")
print(file.readline())  # so if we are at the same dir no need to give the path just file name..it will read 1st line only
print(file.readlines()) #
#readline is for the single line
#readlines for the multiple
