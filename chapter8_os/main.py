import os

# print(os.getcwd()) # get current working directory
# print(os.path.abspath(__file__)) # get absolute path of the current file
# print(os.listdir()) # list all the files and directories in the current directory


# print(os.listdir())



# for i in os.listdir():
#     if os.path.isfile(i):
#         print(f"{i} is a file")
#
#     elif os.path.isdir(i):
#         print(f"{i} is a directory")
#
#     else:
#         print("Directory is Empty...")



# print(os.path.dirname(os.path.abspath(__file__)))
print(os.listdir(os.path.dirname(os.path.abspath(__file__))))
# print(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Data"))

full_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"Data")

for file in os.listdir(full_path):
    print(file)

